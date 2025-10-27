#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para cargar estudiantes de 4° año específicos
Ejecutar: python cargar_estudiantes_4to.py
"""

import sys
import os

# Agregar el directorio App_Web al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'App_Web'))

try:
    from app import conectar_db, DB_NAME
    print("✅ Importaciones exitosas")
    
    # Lista de estudiantes de 4° año
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
    
    def cargar_estudiantes_4to():
        """Carga los estudiantes específicos de 4° año"""
        conn = conectar_db(DB_NAME)
        if not conn:
            print("❌ No se pudo conectar a la base de datos")
            return False
        
        try:
            with conn.cursor() as cursor:
                # Verificar si la tabla estudiantes existe
                cursor.execute("SHOW TABLES LIKE 'estudiantes'")
                if not cursor.fetchone():
                    print("❌ La tabla 'estudiantes' no existe")
                    return False
                
                # Limpiar estudiantes existentes de 4° año (opcional)
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
            print(f"❌ Error cargando estudiantes: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()
    
    def verificar_carga():
        """Verifica que los estudiantes se cargaron correctamente"""
        conn = conectar_db(DB_NAME)
        if not conn:
            return False
        
        try:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT nombre, apellido, dni, email 
                    FROM estudiantes 
                    WHERE curso = '4' 
                    ORDER BY apellido, nombre
                """)
                estudiantes = cursor.fetchall()
                
                print(f"\n📊 Verificación - Estudiantes de 4° año cargados:")
                print("=" * 60)
                for est in estudiantes:
                    print(f"• {est[1]}, {est[0]} - DNI: {est[2]} - Email: {est[3]}")
                print("=" * 60)
                print(f"Total: {len(estudiantes)} estudiantes")
                
        except Exception as e:
            print(f"❌ Error verificando carga: {e}")
        finally:
            conn.close()
    
    # Ejecutar la carga
    print("🚀 Iniciando carga de estudiantes de 4° año...")
    if cargar_estudiantes_4to():
        verificar_carga()
        print("\n✅ ¡Proceso completado exitosamente!")
        print("💡 Ahora puedes ejecutar la aplicación y ver los estudiantes en 'Ver Cursos'")
    else:
        print("\n❌ Error en el proceso de carga")
        
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("💡 Asegúrate de estar en el directorio correcto")
except Exception as e:
    print(f"❌ Error inesperado: {e}")




