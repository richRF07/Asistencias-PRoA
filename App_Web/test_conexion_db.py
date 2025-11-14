#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de diagnóstico para probar la conexión a la base de datos
Ejecutar: python test_conexion_db.py
"""

import pymysql
import sys
from datetime import datetime

# Configuración de la base de datos
DB_CONFIG = {
    "host": "localhost",
    "user": "root", 
    "password": "admin123",
    "database": "asistencia_db",
    "port": 3307,
    "charset": "utf8mb4"
}

def test_conexion_basica():
    """Prueba la conexión básica sin especificar base de datos"""
    print("🔍 Probando conexión básica al servidor MySQL...")
    
    try:
        # Conexión sin especificar base de datos
        conn = pymysql.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            port=DB_CONFIG["port"],
            charset=DB_CONFIG["charset"]
        )
        
        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"✅ Conexión exitosa! Versión MySQL: {version[0]}")
            
            # Listar bases de datos disponibles
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            print(f"📊 Bases de datos disponibles: {[db[0] for db in databases]}")
            
        conn.close()
        return True
        
    except pymysql.err.OperationalError as e:
        print(f"❌ Error de conexión: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_base_datos():
    """Prueba la conexión a la base de datos específica"""
    print("\n🔍 Probando conexión a la base de datos 'asistencia_db'...")
    
    try:
        conn = pymysql.connect(**DB_CONFIG)
        
        with conn.cursor() as cursor:
            # Verificar que la base de datos existe
            cursor.execute("SELECT DATABASE()")
            current_db = cursor.fetchone()
            print(f"✅ Conectado a la base de datos: {current_db[0]}")
            
            # Listar tablas
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print(f"📋 Tablas encontradas: {[table[0] for table in tables]}")
            
            # Verificar estructura de cada tabla
            for table in tables:
                table_name = table[0]
                cursor.execute(f"DESCRIBE {table_name}")
                columns = cursor.fetchall()
                print(f"\n📊 Estructura de '{table_name}':")
                for col in columns:
                    print(f"   - {col[0]} ({col[1]})")
                    
        conn.close()
        return True
        
    except pymysql.err.OperationalError as e:
        print(f"❌ Error de conexión a la base de datos: {e}")
        return False
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

def test_estructura_tablas():
    """Verifica que las tablas tengan la estructura correcta"""
    print("\n🔍 Verificando estructura de tablas...")
    
    try:
        conn = pymysql.connect(**DB_CONFIG)
        
        with conn.cursor() as cursor:
            # Verificar tabla estudiantes
            try:
                cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'estudiantes'")
                columns = [row[0] for row in cursor.fetchall()]
                print(f"📋 Columnas en 'estudiantes': {columns}")
                
                # Verificar columnas esperadas
                expected_columns = ['id', 'nombre', 'apellido', 'dni', 'email', 'telefono', 'fecha_nacimiento', 'curso']
                missing_columns = [col for col in expected_columns if col not in columns]
                if missing_columns:
                    print(f"⚠️  Faltan columnas en 'estudiantes': {missing_columns}")
                else:
                    print("✅ Tabla 'estudiantes' tiene todas las columnas necesarias")
                    
            except Exception as e:
                print(f"❌ Error verificando tabla 'estudiantes': {e}")
                
            # Verificar tabla usuarios
            try:
                cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'usuarios'")
                columns = [row[0] for row in cursor.fetchall()]
                print(f"📋 Columnas en 'usuarios': {columns}")
                
                # Verificar columnas esperadas
                expected_columns = ['id', 'nombre', 'email', 'password']
                missing_columns = [col for col in expected_columns if col not in columns]
                if missing_columns:
                    print(f"⚠️  Faltan columnas en 'usuarios': {missing_columns}")
                else:
                    print("✅ Tabla 'usuarios' tiene todas las columnas necesarias")
                    
            except Exception as e:
                print(f"❌ Error verificando tabla 'usuarios': {e}")
                
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error verificando estructura: {e}")
        return False

def crear_tablas_correctas():
    """Crea las tablas con la estructura correcta"""
    print("\n🔧 Creando/actualizando tablas con estructura correcta...")
    
    try:
        conn = pymysql.connect(**DB_CONFIG)
        
        with conn.cursor() as cursor:
            # Crear tabla usuarios con estructura correcta
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
            """)
            
            # Crear tabla estudiantes con estructura correcta
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS estudiantes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    apellido VARCHAR(100),
                    dni VARCHAR(20),
                    email VARCHAR(100),
                    telefono VARCHAR(20),
                    fecha_nacimiento DATE,
                    curso VARCHAR(10),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
            """)
            
            # Crear tabla asistencias
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS asistencias (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    estudiante_id INT NOT NULL,
                    fecha DATE NOT NULL,
                    estado ENUM('Presente', 'Tarde', 'Ausente', 'Justificado') NOT NULL,
                    observaciones TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id) ON DELETE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
            """)
            
            conn.commit()
            print("✅ Tablas creadas/actualizadas correctamente")
            
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error creando tablas: {e}")
        return False

def main():
    """Función principal de diagnóstico"""
    print("=" * 60)
    print("🔧 DIAGNÓSTICO DE CONEXIÓN A BASE DE DATOS")
    print("=" * 60)
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔗 Configuración: {DB_CONFIG['host']}:{DB_CONFIG['port']}")
    print("=" * 60)
    
    # Paso 1: Probar conexión básica
    if not test_conexion_basica():
        print("\n❌ No se puede conectar al servidor MySQL.")
        print("💡 Verifica que:")
        print("   - XAMPP/WAMP esté ejecutándose")
        print("   - MySQL esté iniciado")
        print("   - El puerto 3307 esté disponible")
        print("   - Las credenciales sean correctas")
        return False
    
    # Paso 2: Probar conexión a la base de datos
    if not test_base_datos():
        print("\n❌ No se puede conectar a la base de datos 'asistencia_db'.")
        print("💡 Verifica que la base de datos exista o créala desde phpMyAdmin")
        return False
    
    # Paso 3: Verificar estructura de tablas
    test_estructura_tablas()
    
    # Paso 4: Ofrecer crear tablas correctas
    print("\n" + "=" * 60)
    respuesta = input("¿Quieres crear/actualizar las tablas con la estructura correcta? (s/n): ")
    if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        if crear_tablas_correctas():
            print("\n✅ ¡Base de datos lista para usar!")
        else:
            print("\n❌ Error creando las tablas")
    else:
        print("\n⚠️  Las tablas pueden tener estructura incorrecta")
    
    print("\n" + "=" * 60)
    print("🏁 Diagnóstico completado")
    print("=" * 60)

if __name__ == "__main__":
    main()






