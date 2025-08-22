from flask import Flask, render_template, request, redirect, flash
from datetime import date
import pymysql

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_flash'

# Conexión a MySQL
def conectar_db():
    return pymysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="asistencia_db"
    )

# Ruta principal con formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el login
@app.route('/login')
def login():
    return render_template('login.html')

# Ruta para el registro
@app.route('/registro')
def registro():
    return render_template('registro.html')

# Ruta para registrar la asistencia
@app.route('/registrar', methods=['POST'])
def registrar():
    curso = request.form.get('curso')
    nombre = request.form.get('nombre')
    fecha = request.form.get('fecha') or date.today().isoformat()
    estado = request.form.get('estado')
    observaciones = request.form.get('observaciones', '')

    if not curso or not nombre or not estado:
        flash("⚠️ Faltan campos obligatorios.")
        return redirect('/')
    conn = None
    cursor = None
    try:
        conn = conectar_db()
        cursor = conn.cursor()

        tabla_estudiantes = f"estudiantes_{curso}"
        tabla_asistencias = f"asistencias_{curso}"

        # Insertar estudiante
        cursor.execute(f"INSERT INTO {tabla_estudiantes} (nombre) VALUES (%s)", (nombre,))
        estudiante_id = cursor.lastrowid

        # Insertar asistencia
        cursor.execute(f"""
            INSERT INTO {tabla_asistencias} (estudiante_id, fecha, estado, observaciones)
            VALUES (%s, %s, %s, %s)
        """, (estudiante_id, fecha, estado, observaciones))

        conn.commit()
        flash("✅ Asistencia registrada correctamente.")
    except Exception as e:
        flash(f"❌ Error al registrar: {e}")
    finally:
        cursor.close()
        conn.close()

    return redirect('/')

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
