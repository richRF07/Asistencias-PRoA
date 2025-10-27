-- =====================================================
-- Script de creación de base de datos para PROA
-- Sistema de Asistencias
-- =====================================================

-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS `asistencia_db` 
DEFAULT CHARACTER SET utf8mb4 
COLLATE utf8mb4_general_ci;

USE `asistencia_db`;

-- =====================================================
-- Tabla: usuarios
-- =====================================================
DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL UNIQUE,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =====================================================
-- Tabla: estudiantes
-- =====================================================
DROP TABLE IF EXISTS `estudiantes`;
CREATE TABLE `estudiantes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `dni` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `curso` varchar(10) DEFAULT NULL,
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_curso` (`curso`),
  KEY `idx_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =====================================================
-- Tabla: asistencias
-- =====================================================
DROP TABLE IF EXISTS `asistencias`;
CREATE TABLE `asistencias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `estudiante_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` enum('Presente','Tarde','Ausente','Justificado') NOT NULL,
  `observaciones` text DEFAULT NULL,
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_estudiante_id` (`estudiante_id`),
  KEY `idx_fecha` (`fecha`),
  KEY `idx_estado` (`estado`),
  CONSTRAINT `asistencias_ibfk_1` 
    FOREIGN KEY (`estudiante_id`) 
    REFERENCES `estudiantes` (`id`) 
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- =====================================================
-- Datos de ejemplo (opcional)
-- =====================================================

-- Insertar algunos estudiantes de ejemplo
INSERT INTO `estudiantes` (`nombre`, `apellido`, `dni`, `email`, `telefono`, `fecha_nacimiento`, `curso`) VALUES
('Juan', 'Pérez', '12345678', 'juan.perez@email.com', '1234567890', '2005-03-15', '1'),
('María', 'González', '87654321', 'maria.gonzalez@email.com', '0987654321', '2005-07-22', '1'),
('Carlos', 'López', '11223344', 'carlos.lopez@email.com', '1122334455', '2004-11-08', '2'),
('Ana', 'Martínez', '44332211', 'ana.martinez@email.com', '4433221155', '2004-12-03', '2'),
('Pedro', 'Rodríguez', '55667788', 'pedro.rodriguez@email.com', '5566778899', '2003-05-18', '3'),
('Laura', 'Fernández', '99887766', 'laura.fernandez@email.com', '9988776655', '2003-09-25', '3');

-- Insertar algunos usuarios de ejemplo
INSERT INTO `usuarios` (`nombre`, `email`, `password`) VALUES
('Admin Sistema', 'admin@proa.edu.ar', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj8VzKz8Kz8K'),
('Profesor 1', 'prof1@proa.edu.ar', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj8VzKz8Kz8K');

-- Insertar algunas asistencias de ejemplo
INSERT INTO `asistencias` (`estudiante_id`, `fecha`, `estado`, `observaciones`) VALUES
(1, CURDATE(), 'Presente', 'Llegó puntual'),
(2, CURDATE(), 'Tarde', 'Llegó 10 minutos tarde'),
(3, CURDATE(), 'Presente', 'Sin observaciones'),
(4, CURDATE(), 'Ausente', 'Falta justificada'),
(5, CURDATE(), 'Presente', 'Participó activamente'),
(6, CURDATE(), 'Justificado', 'Cita médica');

-- =====================================================
-- Verificar la creación
-- =====================================================
SELECT 'Base de datos creada exitosamente' as mensaje;
SELECT COUNT(*) as total_estudiantes FROM estudiantes;
SELECT COUNT(*) as total_usuarios FROM usuarios;
SELECT COUNT(*) as total_asistencias FROM asistencias;

-- Mostrar estructura de las tablas
SHOW TABLES;
DESCRIBE estudiantes;
DESCRIBE usuarios;
DESCRIBE asistencias;


