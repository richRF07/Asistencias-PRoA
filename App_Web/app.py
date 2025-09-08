from flask import Flask, render_template, request, redirect, flash
from datetime import date
import pymysql
import re

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

# Conexión a MySQL
def conectar_db():
    try:
        return pymysql.connect(
            host="localhost",
            user="root",     # Asegurate de que este usuario exista en tu MySQL
            password="root",          # Y que la contraseña sea correcta
            database="asistenciasdb",  # Y que esta base de datos exista
            port=3307         # Cambia si es necesario
        )
    except pymysql.err.OperationalError as e:
        print(f"Error de conexión: {e}")
        return None

def sanitizar_curso(curso: str) -> str:
    """Permite solo letras, números y guiones bajos en el nombre de curso."""
    if not curso:
        return ''
    if not re.fullmatch(r"[A-Za-z0-9_]{1,32}", curso):
        return ''
    return curso

def asegurar_tablas(conn, tabla_estudiantes: str, tabla_asistencias: str):
    """Crea las tablas si no existen para el curso indicado."""
    with conn.cursor() as cursor:
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {tabla_estudiantes} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
        )
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {tabla_asistencias} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                estudiante_id INT NOT NULL,
                fecha DATE NOT NULL,
                estado ENUM('Presente','Ausente','Tarde','Justificado') NOT NULL,
                observaciones VARCHAR(500) DEFAULT '',
                FOREIGN KEY (estudiante_id) REFERENCES {tabla_estudiantes}(id)
                    ON DELETE CASCADE ON UPDATE CASCADE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
        )
        conn.commit()

# Ruta principal con formulario
@app.route('/')
def index():
    return render_template('login.html')

# Ruta para el login
@app.route('/login')
def login():
    return render_template('login.html')

# Ruta para el registro
#@app.route('/registro')
#def registro():
#   return render_template('registro.html')

# Ruta para registrar la asistencia
@app.route('/registro', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        # Muestra el formulario de registro de asistencia
        return render_template('registro.html')  # Cambia por tu template
    # Procesa el formulario de registro de asistencia
    curso = request.form.get('curso')
    nombre = request.form.get('nombre')
    fecha = request.form.get('fecha') or date.today().isoformat()
    estado = request.form.get('estado')
    observaciones = request.form.get('observaciones', '')

    curso = sanitizar_curso(curso)

    if not curso or not nombre or not estado:
        flash("⚠️ Faltan campos obligatorios o el curso tiene caracteres inválidos.")
        return redirect('/')

    conn = None
    try:
        conn = conectar_db()
        if not conn:
            flash("❌ No se pudo conectar a MySQL. Verifica que XAMPP/MySQL esté iniciado, y revisa host/puerto/usuario/contraseña.")
            return redirect('/')

        tabla_estudiantes = f"estudiantes_{curso}"
        tabla_asistencias = f"asistencias_{curso}"

        asegurar_tablas(conn, tabla_estudiantes, tabla_asistencias)

        with conn.cursor() as cursor:
            # Insertar estudiante
            cursor.execute(f"INSERT INTO {tabla_estudiantes} (nombre) VALUES (%s)", (nombre,))
            estudiante_id = cursor.lastrowid

            # Insertar asistencia
            cursor.execute(
                f"""
            INSERT INTO {tabla_asistencias} (estudiante_id, fecha, estado, observaciones)
            VALUES (%s, %s, %s, %s)
        """,
                (estudiante_id, fecha, estado, observaciones),
            )

            conn.commit()
            flash("✅ Asistencia registrada correctamente.")
    except Exception as e:
        if conn:
            try:
                conn.rollback()
            except Exception:
                pass
        flash(f"❌ Error al registrar: {e}")
    finally:
        if conn:
            try:
                conn.close()
            except Exception:
                pass

    return redirect('/')

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
        flash("Las contraseñas no coinciden")
        return redirect('/registro')

    conexion = conectar_db()
    if not conexion:
        flash("❌ Error de conexión a la base de datos.")
        return redirect('/registro')
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, email, password))
            conexion.commit()
        flash("✅ Usuario registrado correctamente.")
    except Exception as e:
        flash(f"❌ Error al registrar usuario: {e}")
    finally:
        conexion.close()
    return redirect('/login')

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)