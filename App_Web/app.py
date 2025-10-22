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
DB_NAME = "asistencia_db"
DB_PORT = 3306  # Puerto correcto según el archivo SQL

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
            charset='utf8mb4',
            autocommit=True,
            connect_timeout=10
        )
        return conn
    except pymysql.err.OperationalError as e:
        error_msg = f"Error de conexión a MySQL: {e}"
        print(error_msg)
        print(f"Configuración: {DB_HOST}:{DB_PORT}, usuario: {DB_USER}, BD: {db_name}")
        print("💡 Verifica que:")
        print("   - XAMPP/WAMP esté ejecutándose")
        print("   - MySQL esté iniciado en el puerto 3307")
        print("   - Las credenciales sean correctas")
        print("   - La base de datos 'asistencia_db' exista")
        return None
    except Exception as e:
        print(f"Error inesperado de conexión: {e}")
        return None

# ----- FUNCIONES AUXILIARES -----
def sanitizar_curso(curso: str) -> str:
    """Permite letras, números, espacios, guiones y guiones bajos en el nombre de curso."""
    if not curso:
        return ''
    if not re.fullmatch(r"[A-Za-z0-9 _-]{1,32}", curso):
        return ''
    return curso

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

# ----- LISTADO POR CURSO -----
def obtener_estudiantes_por_curso():
    """Devuelve un diccionario { '1': [estudiantes], ..., '6': [...] }"""
    conn = conectar_db(DB_NAME)
    cursos = {str(i): [] for i in range(1, 7)}
    
    if not conn:
        print("❌ No se pudo conectar a la base de datos para obtener estudiantes por curso")
        return cursos
    
    try:
        with conn.cursor() as cursor:
            # Verificar si la tabla estudiantes existe
            cursor.execute("SHOW TABLES LIKE 'estudiantes'")
            if not cursor.fetchone():
                print("⚠️ La tabla 'estudiantes' no existe")
                return cursos
            
            # Obtener estudiantes por curso
            cursor.execute("""
                SELECT id, nombre, apellido, dni, curso
                FROM estudiantes
                WHERE curso IN ('1','2','3','4','5','6')
                ORDER BY CAST(curso AS UNSIGNED), apellido IS NULL, apellido, nombre
            """)
            
            estudiantes = cursor.fetchall()
            print(f"📊 Encontrados {len(estudiantes)} estudiantes en la base de datos")
            
            for row in estudiantes:
                est = {
                    "id": row[0],
                    "nombre": row[1] or "Sin nombre",
                    "apellido": row[2] or "",
                    "dni": row[3] or "",
                    "curso": row[4] or "Sin curso",
                }
                key = str(est.get("curso") or "")
                if key in cursos:
                    cursos[key].append(est)
                else:
                    print(f"⚠️ Curso '{key}' no válido para estudiante {est['nombre']}")
                    
    except Exception as e:
        print(f"❌ Error obteniendo estudiantes por curso: {e}")
    finally:
        conn.close()
    
    # Mostrar resumen
    total_estudiantes = sum(len(estudiantes) for estudiantes in cursos.values())
    print(f"📈 Total de estudiantes organizados: {total_estudiantes}")
    for curso, estudiantes in cursos.items():
        print(f"   Curso {curso}: {len(estudiantes)} estudiantes")
    
    return cursos

# ----- FUNCIÓN PARA DATOS DE PRUEBA -----
def crear_datos_prueba():
    """Crea datos de prueba si no hay estudiantes en la base de datos"""
    conn = conectar_db(DB_NAME)
    if not conn:
        return False
    
    try:
        with conn.cursor() as cursor:
            # Verificar si ya hay estudiantes
            cursor.execute("SELECT COUNT(*) FROM estudiantes")
            count = cursor.fetchone()[0]
            
            if count > 0:
                print(f"✅ Ya hay {count} estudiantes en la base de datos")
                return True
            
            print("📝 No hay estudiantes en la base de datos")
            print("💡 Usa el botón 'Cargar 4° Año' para agregar estudiantes específicos")
            return True
            
    except Exception as e:
        print(f"❌ Error creando datos de prueba: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

# ----- FUNCIÓN PARA CARGAR ESTUDIANTES ESPECÍFICOS DE 4° AÑO -----
def cargar_estudiantes_4to_especificos():
    """Carga los estudiantes específicos de 4° año proporcionados por el usuario"""
    conn = conectar_db(DB_NAME)
    if not conn:
        return False
    
    try:
        with conn.cursor() as cursor:
            # Lista específica de estudiantes de 4° año
            estudiantes_4to = [
                "Barrionuevo Candela",
                "Barrionuevo Martina", 
                "Brizuela Sofia Mariel Luz",
                "Castaño Giovana Alejo",
                "Castillo Mia Brisa",
                "Coolino Gomez Luisana",
                "Gallay Yair Eliel",
                "Gontero Kyara Alejandra",
                "Grinovero Bautista",
                "Guevara Kurozaki Alejandro Luis",
                "Illarraga Gonzalez Luis Felipe",
                "Leone Barrionuevo Franco",
                "Lopez Joaquin",
                "Lujan Della Vedova Pedro",
                "Marratin Lola",
                "Pino Malena Guillermina",
                "Raffos Joaquin",
                "Renoso Thiago Joel",
                "Romero Marcos Valentin",
                "Serminatti Alejo Andre",
                "Torres Martias",
                "Vergara Sofia Magdalena",
                "Zalazar Lucila"
            ]
            
            # Limpiar estudiantes existentes de 4° año
            cursor.execute("DELETE FROM estudiantes WHERE curso = '4'")
            print(f"🗑️ Eliminados estudiantes existentes de 4° año")
            
            # Insertar nuevos estudiantes
            estudiantes_insertados = 0
            for nombre_completo in estudiantes_4to:
                # Separar nombre y apellido
                partes = nombre_completo.strip().split()
                if len(partes) >= 2:
                    nombre = partes[0]
                    apellido = " ".join(partes[1:])  # El resto es el apellido
                    
                    # Generar email basado en el nombre
                    email = f"{nombre.lower()}.{apellido.lower().replace(' ', '.')}@proa.edu.ar"
                    
                    # Generar DNI ficticio (8 dígitos)
                    dni = f"{20000000 + estudiantes_insertados + 1}"
                    
                    # Insertar estudiante
                    cursor.execute("""
                        INSERT INTO estudiantes (nombre, apellido, dni, email, curso)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (nombre, apellido, dni, email, "4"))
                    
                    estudiantes_insertados += 1
                    print(f"✅ Insertado: {apellido}, {nombre}")
            
            conn.commit()
            print(f"\n🎉 ¡Cargados {estudiantes_insertados} estudiantes de 4° año!")
            return True
            
    except Exception as e:
        print(f"❌ Error cargando estudiantes de 4° año: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

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

# Perfil por ID directo (sin requerir sesión) para usar desde "Ver perfil"
@app.route('/estudiante/<int:estudiante_id>')
def perfil_estudiante_publico(estudiante_id: int):
    estudiante = obtener_estudiante_por_id(estudiante_id)
    if not estudiante:
        flash('Estudiante no encontrado.')
        return redirect(url_for('index'))
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
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
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

# Listado de alumnos por curso (1° a 6°)
@app.route('/cursos')
def listar_cursos():
    try:
        print("🔍 Accediendo a la vista de cursos...")
        
        # Intentar crear datos de prueba si no hay estudiantes
        crear_datos_prueba()
        
        cursos_dict = obtener_estudiantes_por_curso()
        
        # Verificar si hay estudiantes
        total_estudiantes = sum(len(estudiantes) for estudiantes in cursos_dict.values())
        if total_estudiantes == 0:
            flash("ℹ️ No hay estudiantes registrados en ningún curso. Puedes agregar estudiantes desde 'Registrar Asistencia'.")
        
        print(f"✅ Preparando vista con {total_estudiantes} estudiantes")
        return render_template('listas_cursos.html', cursos=cursos_dict)
        
    except Exception as e:
        print(f"❌ Error en la vista de cursos: {e}")
        flash(f"❌ Error al cargar la lista de cursos: {e}")
        # Devolver diccionario vacío en caso de error
        cursos_vacios = {str(i): [] for i in range(1, 7)}
        return render_template('listas_cursos.html', cursos=cursos_vacios)

# Ruta para cargar estudiantes específicos de 4° año
@app.route('/cargar_4to')
def cargar_estudiantes_4to():
    try:
        print("🚀 Cargando estudiantes específicos de 4° año...")
        if cargar_estudiantes_4to_especificos():
            flash("✅ Estudiantes de 4° año cargados exitosamente!")
        else:
            flash("❌ Error al cargar estudiantes de 4° año")
        return redirect(url_for('listar_cursos'))
    except Exception as e:
        print(f"❌ Error en la ruta de carga: {e}")
        flash(f"❌ Error: {e}")
        return redirect(url_for('listar_cursos'))

@app.route('/registro', methods=['GET', 'POST'])
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


@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():
    if request.method == 'GET':
        return render_template('registro_usuario.html')
    
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if not nombre or not email or not password or not confirm_password:
        flash("⚠️ Todos los campos son obligatorios.")
        return redirect('/registro_usuario')

    if password != confirm_password:
        flash("⚠️ Las contraseñas no coinciden.")
        return redirect('/registro_usuario')

    conn = conectar_db(DB_NAME)
    if not conn:
        flash("❌ Error de conexión a la base de datos.")
        return redirect('/registro_usuario')

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