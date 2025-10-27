from flask import Flask, render_template, request, redirect, flash
from datetime import date
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

# ----- CONFIGURACIÓN DE BASE DE DATOS -----
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "admin123"
DB_NAME = "asistencias_db"
DB_PORT = 3307  # Cambiar solo si MySQL usa otro puerto

# ----- CONEXIÓN A MYSQL -----
def conectar_db(db_name=None):
    """Conecta a MySQL. Si db_name es None, no selecciona base de datos."""
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=db_name,
            port=DB_PORT,
            charset='utf8mb4'
        )
        return conn
    except pymysql.err.OperationalError as e:
        print(f"Error de conexión: {e}")
        return None

# ----- FUNCIONES AUXILIARES -----
def sanitizar_curso(curso: str) -> str:
    """Permite letras, números, espacios, guiones y guiones bajos en el nombre de curso."""
    if not curso:
        return ''
    if not re.fullmatch(r"[A-Za-z0-9 _-]{1,32}", curso):
        return ''
    return curso

# ----- LISTADO POR CURSO -----
def obtener_estudiantes_por_curso():
    """Devuelve un diccionario con cursos y sus estudiantes"""
    conn = conectar_db(DB_NAME)
    
    if not conn:
        print("❌ No se pudo conectar a la base de datos para obtener estudiantes por curso")
        return {}
    
    try:
        with conn.cursor() as cursor:
            # Primero obtener todos los cursos de la tabla cursos
            cursor.execute("SELECT id, nombre FROM cursos ORDER BY id")
            cursos_db = cursor.fetchall()
            
            print(f"📚 Encontrados {len(cursos_db)} cursos en la base de datos")
            
            # Crear diccionario de cursos con sus estudiantes
            cursos_dict = {}
            
            for curso_row in cursos_db:
                curso_id = curso_row[0]
                curso_nombre = curso_row[1]
                
                # Obtener estudiantes de este curso
                cursor.execute("""
                    SELECT id_Est, Apellido, nombre, DNI, email_Est
                    FROM estudiantes
                    WHERE curso_id = %s
                    ORDER BY Apellido, nombre
                """, (curso_id,))
                
                estudiantes = cursor.fetchall()
                
                estudiantes_list = []
                for est in estudiantes:
                    estudiantes_list.append({
                        "id": est[0],
                        "apellido": est[1] or "",
                        "nombre": est[2] or "Sin nombre",
                        "dni": est[3] or "",
                        "email": est[4] or "",
                    })
                
                # Usar el id del curso como clave
                cursos_dict[str(curso_id)] = {
                    "id": curso_id,
                    "nombre": curso_nombre,
                    "estudiantes": estudiantes_list
                }
                
                print(f"   Curso {curso_id} ({curso_nombre}): {len(estudiantes_list)} estudiantes")
            
            return cursos_dict
                    
    except Exception as e:
        print(f"❌ Error obteniendo estudiantes por curso: {e}")
        import traceback
        traceback.print_exc()
        return {}
    finally:
        conn.close()

# ----- PERFIL ESTUDIANTE -----
def obtener_estudiante_por_id(estudiante_id):
    conn = conectar_db(DB_NAME)
    if not conn:
        return None
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id, nombre, apellido, dni, email, telefono, fecha_nacimiento FROM estudiantes WHERE id=%s", (estudiante_id,))
            row = cursor.fetchone()
            if row:
                keys = ["id", "nombre", "apellido", "dni", "email", "telefono", "fecha_nacimiento"]
                return dict(zip(keys, row))
    finally:
        conn.close()
    return None

def obtener_asistencias_estudiante(estudiante_id):
    conn = conectar_db(DB_NAME)
    if not conn:
        return []
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT a.fecha, e.curso, a.estado, a.observaciones
                FROM asistencias a
                JOIN estudiantes e ON a.estudiante_id = e.id
                WHERE a.estudiante_id = %s
                ORDER BY a.fecha DESC
            """, (estudiante_id,))
            return [
                {"fecha": r[0], "curso": r[1], "estado": r[2], "observaciones": r[3]} for r in cursor.fetchall()
            ]
    finally:
        conn.close()
    return []
# ----- RUTAS -----

# Ruta para mostrar el perfil del estudiante
from flask import session, url_for
@app.route('/perfil')
def perfil_estudiante():
    estudiante_id = session.get('estudiante_id')
    if not estudiante_id:
        flash('Debes iniciar sesión para ver tu perfil.')
        return redirect(url_for('login'))
    estudiante = obtener_estudiante_por_id(estudiante_id)
    asistencias = obtener_asistencias_estudiante(estudiante_id)
    return render_template('perfil_estudiante.html', estudiante=estudiante, asistencias=asistencias)

# Ruta para actualizar datos del perfil
@app.route('/actualizar_perfil', methods=['POST'])
def actualizar_perfil():
    estudiante_id = session.get('estudiante_id')
    if not estudiante_id:
        flash('Debes iniciar sesión para modificar tu perfil.')
        return redirect(url_for('login'))
    campos = ['nombre', 'apellido', 'dni', 'email', 'telefono', 'fecha_nacimiento']
    datos = {campo: request.form.get(campo) for campo in campos}
    conn = conectar_db(DB_NAME)
    if not conn:
        flash('No se pudo conectar a la base de datos.')
        return redirect(url_for('perfil_estudiante'))
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE estudiantes SET nombre=%s, apellido=%s, dni=%s, email=%s, telefono=%s, fecha_nacimiento=%s
                WHERE id=%s
            """, (datos['nombre'], datos['apellido'], datos['dni'], datos['email'], datos['telefono'], datos['fecha_nacimiento'], estudiante_id))
            conn.commit()
        flash('✅ Perfil actualizado correctamente.')
    except Exception as e:
        conn.rollback()
        print(f"ERROR al actualizar perfil: {e}")
        flash(f"❌ Error al actualizar perfil: {e}")
    finally:
        conn.close()
    return redirect(url_for('perfil_estudiante'))

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada correctamente.')
    return redirect(url_for('login'))

# Listado de alumnos por curso (desde la tabla cursos)
@app.route('/cursos')
def listar_cursos():
    try:
        print("🔍 Accediendo a la vista de cursos...")
        
        cursos_dict = obtener_estudiantes_por_curso()
        
        # Verificar si hay cursos
        if not cursos_dict:
            flash("ℹ️ No hay cursos registrados en la base de datos.")
        
        print(f"✅ Preparando vista con {len(cursos_dict)} cursos")
        return render_template('listas_cursos.html', cursos=cursos_dict)
        
    except Exception as e:
        print(f"❌ Error en la vista de cursos: {e}")
        import traceback
        traceback.print_exc()
        flash(f"❌ Error al cargar la lista de cursos: {e}")
        return render_template('listas_cursos.html', cursos={})

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('index.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not email or not password:
            flash('⚠️ Debes ingresar email y contraseña.')
            return redirect(url_for('login'))
        conn = conectar_db(DB_NAME)
        if not conn:
            flash('❌ Error de conexión a la base de datos.')
            return redirect(url_for('login'))
        try:
            with conn.cursor() as cursor:
                # Buscar usuario en la tabla usuarios
                cursor.execute("SELECT id, password FROM usuarios WHERE email=%s", (email,))
                user = cursor.fetchone()
                if user and check_password_hash(user[1], password):
                    # Buscar estudiante correspondiente (por email)
                    cursor.execute("SELECT id FROM estudiantes WHERE email=%s", (email,))
                    estudiante = cursor.fetchone()
                    if estudiante:
                        session['estudiante_id'] = estudiante[0]
                        flash('Bienvenido/a!')
                        return redirect(url_for('perfil_estudiante'))
                    else:
                        flash('No se encontró un estudiante asociado a este email.')
                        return redirect(url_for('login'))
                else:
                    flash('Email o contraseña incorrectos.')
                    return redirect(url_for('login'))
        except Exception as e:
            print(f"ERROR en login: {e}")
            flash('❌ Error al iniciar sesión.')
            return redirect(url_for('login'))
        finally:
            conn.close()
    # Si es GET, muestra el formulario de login
    return render_template('login.html')

|1@app.route('/registro', methods=['GET', 'POST'])
def registrar_asistencia():
    if request.method == 'POST':
        # Datos del formulario
        curso = sanitizar_curso(request.form.get('curso'))
        nombre = request.form.get('nombre')
        dni = request.form.get('dni')
        fecha = request.form.get('fecha') or date.today().isoformat()
        estado = request.form.get('estado')
        observaciones = request.form.get('observaciones', '')

        print(f"DEBUG -> curso={curso}, nombre={nombre}, dni={dni}, fecha={fecha}, estado={estado}, observaciones={observaciones}")

        if not curso or not nombre or not estado or not dni:
            flash("⚠️ Faltan campos obligatorios o el curso tiene caracteres inválidos.")
            return redirect('/registro')

        conn = conectar_db(DB_NAME)
        if not conn:
            flash("❌ No se pudo conectar a MySQL. Verifica que XAMPP/MySQL esté iniciado, y revisa host/puerto/usuario/contraseña.")
            return redirect('/registro')

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM estudiantes WHERE nombre=%s AND curso=%s AND dni=%s",
                    (nombre, curso, dni)
                )
                resultado = cursor.fetchone()
                if resultado:
                    estudiante_id = resultado[0]
                else:
                    cursor.execute(
                        "INSERT INTO estudiantes (nombre, curso, dni) VALUES (%s, %s, %s)",
                        (nombre, curso, dni)
                    )
                    estudiante_id = cursor.lastrowid

                cursor.execute(
                    "INSERT INTO asistencias (estudiante_id, fecha, estado, observaciones) VALUES (%s, %s, %s, %s)",
                    (estudiante_id, fecha, estado, observaciones)
                )
                conn.commit()
                flash("✅ Asistencia registrada correctamente.")
  # Guardar el estudiante_id en la sesión para mostrar su perfil
                from flask import session
                session['estudiante_id'] = estudiante_id

        except Exception as e:
            conn.rollback()
            print(f"ERROR en registrar_asistencia: {e}")
            flash(f"❌ Error al registrar: {e}")
            return redirect('/registro')
        finally:
            conn.close()

        # Redirigir al perfil del estudiante (listado de asistencias)
        return redirect('/perfil')
    # Si es GET, solo muestra el formulario
    return render_template('index.html')


@app.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if not nombre or not email or not password or not confirm_password:
        flash("⚠️ Todos los campos son obligatorios.")
        return redirect('/registro')

    if password != confirm_password:
        flash("⚠️ Las contraseñas no coinciden.")
        return redirect('/registro')

    conn = conectar_db(DB_NAME)
    if not conn:
        flash("❌ Error de conexión a la base de datos.")
        return redirect('/registro')

    try:
        hashed_password = generate_password_hash(password)
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)",
                (nombre, email, hashed_password)
            )
            conn.commit()
        flash("✅ Usuario registrado correctamente.")
    except pymysql.err.IntegrityError:
        flash("⚠️ El email ya está registrado.")
    except Exception as e:
        print(f"ERROR en registrar_usuario: {e}")  # --- DEBUG en consola ---
        flash(f"❌ Error al registrar usuario: {e}")
    finally:
        conn.close()

    return redirect('/login')

# ----- EJECUCIÓN -----
if __name__ == '__main__':

    app.run(debug=True)