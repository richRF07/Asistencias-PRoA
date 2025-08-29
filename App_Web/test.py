import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="root",  # O "" si no tienes contraseña
        database="asistenciasdb",
        port=3306         # Cambia si es necesario
    )
    print("Conexión exitosa")
    conn.close()
except Exception as e:
    print(f"Error: {e}")