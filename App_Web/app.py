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
# ----- RUTAS -----
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registrar_asistencia():
    if request.method == 'POST':
        # Datos del formulario
        curso = sanitizar_curso(request.form.get('curso'))
        nombre = request.form.get('nombre')
        fecha = request.form.get('fecha') or date.today().isoformat()
        estado = request.form.get('estado')
        observaciones = request.form.get('observaciones', '')

        print(f"DEBUG -> curso={curso}, nombre={nombre}, fecha={fecha}, estado={estado}, observaciones={observaciones}")

        if not curso or not nombre or not estado:
            flash("⚠️ Faltan campos obligatorios o el curso tiene caracteres inválidos.")
            return redirect('/registro')

        conn = conectar_db(DB_NAME)
        if not conn:
            flash("❌ No se pudo conectar a MySQL. Verifica que XAMPP/MySQL esté iniciado, y revisa host/puerto/usuario/contraseña.")
            return redirect('/registro')

        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM estudiantes WHERE nombre=%s AND curso=%s",
                    (nombre, curso)
                )
                resultado = cursor.fetchone()
                if resultado:
                    estudiante_id = resultado[0]
                else:
                    cursor.execute(
                        "INSERT INTO estudiantes (nombre, curso) VALUES (%s, %s)",
                        (nombre, curso)
                    )
                    estudiante_id = cursor.lastrowid

                cursor.execute(
                    "INSERT INTO asistencias (estudiante_id, fecha, estado, observaciones) VALUES (%s, %s, %s, %s)",
                    (estudiante_id, fecha, estado, observaciones)
                )
                conn.commit()
                flash("✅ Asistencia registrada correctamente.")
        except Exception as e:
            conn.rollback()
            print(f"ERROR en registrar_asistencia: {e}")
            flash(f"❌ Error al registrar: {e}")
        finally:
            conn.close()

        return redirect('/registro')
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
