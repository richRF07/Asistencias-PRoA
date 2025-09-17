import pymysql

# Conexión a la base de datos
conn = pymysql.connect(
    host="localhost",
    user="root",     # Asegurate de que este usuario exista en tu MySQL
    password="root", # Y que la contraseña sea correcta
    database="asistencia_db",  # Y que esta base de datos exista
    port=3307        # Cambia si es necesario
)

cursor = conn.cursor()

# -------------------------------
# Crear tabla de usuarios
# -------------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'docente', 'alumno') NOT NULL DEFAULT 'alumno'
) ENGINE=InnoDB;
''')

# -------------------------------
# Crear tabla de cursos
# -------------------------------
cursor.execute('''
CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT
) ENGINE=InnoDB;
''')

# -------------------------------
# Crear tablas para cada curso (del 1 al 6)
# -------------------------------
for curso in range(1, 7):
    nombre_tabla_est = f"estudiantes_{curso}"
    nombre_tabla_asis = f"asistencias_{curso}"

    # Crear tabla de estudiantes
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {nombre_tabla_est} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        curso_id INT,
        FOREIGN KEY (curso_id) REFERENCES cursos(id)
            ON DELETE CASCADE
    ) ENGINE=InnoDB;
    ''')

    # Crear tabla de asistencias
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {nombre_tabla_asis} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        estudiante_id INT,
        fecha DATE NOT NULL,
        estado ENUM('Presente', 'Tarde', 'Ausente', 'Justificado') NOT NULL,
        observaciones TEXT,
        FOREIGN KEY (estudiante_id) REFERENCES {nombre_tabla_est}(id)
            ON DELETE CASCADE
    ) ENGINE=InnoDB;
    ''')

# Confirmar cambios y cerrar conexión
conn.commit()
cursor.close()
conn.close()

print("✅ Base de datos, tablas de usuarios, cursos y estudiantes creadas correctamente.")