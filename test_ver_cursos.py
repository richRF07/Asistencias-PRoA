#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba rápida para el botón "Ver Cursos"
Ejecutar: python test_ver_cursos.py
"""

import sys
import os

# Agregar el directorio App_Web al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'App_Web'))

try:
    from app import obtener_estudiantes_por_curso, crear_datos_prueba, conectar_db, DB_NAME
    print("✅ Importaciones exitosas")
    
    # Probar conexión
    print("\n🔍 Probando conexión a la base de datos...")
    conn = conectar_db(DB_NAME)
    if conn:
        print("✅ Conexión exitosa")
        conn.close()
    else:
        print("❌ Error de conexión")
        sys.exit(1)
    
    # Crear datos de prueba
    print("\n📝 Creando datos de prueba...")
    if crear_datos_prueba():
        print("✅ Datos de prueba creados/verificados")
    else:
        print("❌ Error creando datos de prueba")
    
    # Probar función de obtener estudiantes
    print("\n📊 Probando función obtener_estudiantes_por_curso...")
    cursos = obtener_estudiantes_por_curso()
    
    total_estudiantes = sum(len(estudiantes) for estudiantes in cursos.values())
    print(f"✅ Total de estudiantes encontrados: {total_estudiantes}")
    
    for curso, estudiantes in cursos.items():
        print(f"   Curso {curso}: {len(estudiantes)} estudiantes")
        for est in estudiantes[:3]:  # Mostrar solo los primeros 3
            print(f"     - {est['apellido']} {est['nombre']} (DNI: {est['dni']})")
        if len(estudiantes) > 3:
            print(f"     ... y {len(estudiantes) - 3} más")
    
    print("\n🎉 ¡El botón 'Ver Cursos' debería funcionar correctamente!")
    print("💡 Ahora puedes ejecutar 'python app.py' y probar la funcionalidad")
    
except ImportError as e:
    print(f"❌ Error de importación: {e}")
    print("💡 Asegúrate de estar en el directorio correcto")
except Exception as e:
    print(f"❌ Error inesperado: {e}")






