-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 14-11-2025 a las 19:08:14
-- Versión del servidor: 10.4.6-MariaDB
-- Versión de PHP: 7.2.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `asistencia_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asistencias`
--

CREATE TABLE `asistencias` (
  `id` int(11) NOT NULL,
  `estudiante_id` int(11) DEFAULT NULL,
  `fecha` date NOT NULL,
  `estado` enum('Presente','Tarde','Ausente','Justificado') NOT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `asistencias`
--

INSERT INTO `asistencias` (`id`, `estudiante_id`, `fecha`, `estado`, `observaciones`) VALUES
(1, 1, '2025-10-27', 'Ausente', 'turno al medico'),
(2, 2, '2025-10-27', 'Tarde', 'llegada tarde por colectivo'),
(3, 3, '2025-10-29', 'Presente', 'ok'),
(4, 4, '2025-10-29', 'Presente', 'ok'),
(5, 5, '2025-10-29', 'Presente', 'ok'),
(6, 6, '2025-10-29', 'Presente', 'ok'),
(7, 7, '2025-10-29', 'Presente', 'ok'),
(8, 8, '2025-10-29', 'Presente', 'ok'),
(9, 9, '2025-10-29', 'Presente', 'ok'),
(10, 10, '2025-10-29', 'Presente', 'ok'),
(11, 11, '2025-10-29', 'Presente', 'ok'),
(12, 12, '2025-10-29', 'Presente', 'ok'),
(13, 13, '2025-10-29', 'Presente', 'ok'),
(14, 14, '2025-10-29', 'Presente', 'ok'),
(15, 15, '2025-10-29', 'Presente', 'ok'),
(16, 16, '2025-10-29', 'Presente', 'ok'),
(17, 17, '2025-10-29', 'Presente', 'ok'),
(18, 18, '2025-10-29', 'Presente', 'ok'),
(19, 19, '2025-10-29', 'Presente', 'ok'),
(20, 20, '2025-10-29', 'Presente', 'ok'),
(21, 21, '2025-10-29', 'Presente', 'ok'),
(22, 22, '2025-10-29', 'Presente', 'ok'),
(23, 23, '2025-10-29', 'Presente', 'ok'),
(24, 24, '2025-10-29', 'Presente', 'ok'),
(25, 25, '2025-10-29', 'Presente', 'ok'),
(26, 26, '2025-10-29', 'Presente', 'ok'),
(27, 27, '2025-10-29', 'Presente', 'ok'),
(28, 28, '2025-10-29', 'Presente', 'ok'),
(29, 29, '2025-10-29', 'Presente', 'ok'),
(30, 30, '2025-10-29', 'Presente', 'ok'),
(31, 31, '2025-10-29', 'Presente', 'ok'),
(32, 32, '2025-10-29', 'Presente', 'ok'),
(33, 33, '2025-10-29', 'Presente', 'ok'),
(34, 34, '2025-10-29', 'Presente', 'ok'),
(35, 35, '2025-10-29', 'Presente', 'ok'),
(36, 36, '2025-10-29', 'Presente', 'ok'),
(37, 37, '2025-10-29', 'Presente', 'ok'),
(38, 38, '2025-10-29', 'Presente', 'ok'),
(39, 39, '2025-10-29', 'Presente', 'ok'),
(40, 40, '2025-10-29', 'Presente', 'ok'),
(41, 41, '2025-10-29', 'Presente', 'ok'),
(42, 42, '2025-10-29', 'Presente', 'ok'),
(43, 43, '2025-10-29', 'Presente', 'ok'),
(44, 44, '2025-10-29', 'Presente', 'ok'),
(45, 45, '2025-10-29', 'Presente', 'ok'),
(46, 46, '2025-10-29', 'Presente', 'ok'),
(47, 47, '2025-10-29', 'Presente', 'ok'),
(48, 48, '2025-10-29', 'Presente', 'ok'),
(49, 49, '2025-10-29', 'Presente', 'ok'),
(50, 50, '2025-10-29', 'Presente', 'ok'),
(51, 51, '2025-10-29', 'Presente', 'ok'),
(52, 52, '2025-10-29', 'Presente', 'ok'),
(53, 53, '2025-10-29', 'Presente', 'ok'),
(54, 54, '2025-10-29', 'Presente', 'ok'),
(55, 55, '2025-10-29', 'Presente', 'ok'),
(56, 56, '2025-10-29', 'Presente', 'ok'),
(57, 57, '2025-10-29', 'Presente', 'ok'),
(58, 58, '2025-10-29', 'Presente', 'ok'),
(59, 59, '2025-10-29', 'Presente', 'ok'),
(60, 60, '2025-10-29', 'Presente', 'ok'),
(61, 61, '2025-10-29', 'Presente', 'ok'),
(62, 62, '2025-10-29', 'Presente', 'ok'),
(63, 63, '2025-10-29', 'Presente', 'ok'),
(64, 63, '2025-10-29', 'Presente', 'ok'),
(65, 64, '2025-10-29', 'Presente', 'ok'),
(66, 65, '2025-10-29', 'Presente', 'ok'),
(67, 66, '2025-10-29', 'Presente', 'ok'),
(68, 67, '2025-10-29', 'Presente', 'ok'),
(69, 68, '2025-10-29', 'Presente', 'ok'),
(70, 69, '2025-10-29', 'Presente', 'ok'),
(71, 70, '2025-10-29', 'Presente', 'ok'),
(72, 71, '2025-10-29', 'Presente', 'ok'),
(73, 72, '2025-10-29', 'Presente', 'ok'),
(74, 73, '2025-10-29', 'Presente', 'ok'),
(75, 74, '2025-10-29', 'Presente', 'ok'),
(76, 75, '2025-10-29', 'Presente', 'ok'),
(77, 76, '2025-10-29', 'Presente', 'ok'),
(78, 77, '2025-10-29', 'Presente', 'ok'),
(79, 78, '2025-10-29', 'Presente', 'ok'),
(80, 79, '2025-10-29', 'Presente', 'ok'),
(81, 80, '2025-10-29', 'Presente', 'ok\r\n'),
(82, 81, '2025-10-29', 'Presente', 'ok'),
(83, 82, '2025-10-29', 'Presente', 'ok'),
(84, 83, '2025-10-29', 'Presente', 'ok'),
(85, 84, '2025-10-29', 'Presente', 'ok'),
(86, 85, '2025-10-29', 'Presente', 'ok'),
(87, 86, '2025-10-29', 'Presente', 'ok'),
(88, 87, '2025-10-29', 'Presente', 'ok'),
(89, 88, '2025-10-29', 'Presente', 'ok'),
(90, 89, '2025-10-29', 'Presente', 'ok'),
(91, 90, '2025-10-29', 'Presente', 'ok'),
(92, 91, '2025-10-29', 'Presente', 'ok'),
(93, 92, '2025-10-29', 'Presente', 'ok'),
(94, 93, '2025-10-29', 'Presente', 'ok'),
(95, 94, '2025-10-29', 'Presente', 'ok'),
(96, 95, '2025-10-29', 'Presente', 'ok'),
(97, 96, '2025-10-29', 'Presente', 'ok'),
(98, 97, '2025-10-29', 'Presente', 'ok'),
(99, 98, '2025-10-29', 'Presente', 'ok'),
(100, 99, '2025-10-29', 'Presente', 'ok'),
(101, 100, '2025-10-29', 'Presente', 'ok'),
(102, 101, '2025-10-29', 'Presente', 'ok'),
(103, 102, '2025-10-29', 'Presente', 'ok'),
(104, 103, '2025-10-29', 'Presente', 'ok'),
(105, 104, '2025-10-29', 'Presente', 'ok'),
(106, 105, '2025-10-29', 'Presente', 'ok'),
(107, 106, '2025-10-29', 'Presente', 'ok'),
(108, 107, '2025-10-29', 'Presente', 'ok'),
(109, 108, '2025-10-29', 'Presente', 'ok'),
(110, 109, '2025-10-29', 'Presente', 'ok'),
(111, 110, '2025-10-29', 'Presente', 'ok'),
(112, 111, '2025-10-29', 'Presente', 'ok'),
(113, 112, '2025-10-29', 'Presente', 'ok'),
(114, 113, '2025-10-29', 'Presente', 'ok'),
(115, 114, '2025-10-29', 'Presente', 'ok'),
(116, 115, '2025-10-29', 'Presente', 'ok'),
(117, 116, '2025-10-29', 'Presente', 'ok\r\n'),
(118, 117, '2025-10-29', 'Presente', 'ok'),
(119, 118, '2025-10-29', 'Presente', 'ok'),
(120, 119, '2025-10-29', 'Presente', 'ok'),
(121, 120, '2025-10-29', 'Presente', 'ok'),
(122, 121, '2025-10-29', 'Presente', 'ok'),
(123, 122, '2025-10-29', 'Presente', 'ok'),
(124, 123, '2025-10-29', 'Presente', 'ok'),
(125, 124, '2025-10-29', 'Presente', 'ok'),
(126, 125, '2025-10-29', 'Presente', 'ok'),
(127, 126, '2025-10-29', 'Presente', 'ok'),
(128, 127, '2025-10-29', 'Presente', 'ok'),
(129, 128, '2025-10-29', 'Presente', 'ok'),
(130, 129, '2025-10-29', 'Presente', 'ok'),
(131, 130, '2025-10-29', 'Presente', 'ok'),
(132, 131, '2025-10-29', 'Presente', 'ok'),
(133, 132, '2025-10-29', 'Presente', 'ok'),
(134, 133, '2025-10-29', 'Presente', 'ok'),
(135, 134, '2025-10-29', 'Presente', 'ok'),
(136, 135, '2025-10-29', 'Presente', 'ok'),
(137, 136, '2025-10-29', 'Presente', 'ok'),
(138, 137, '2025-10-29', 'Presente', 'ok'),
(139, 138, '2025-10-29', 'Presente', 'ok'),
(140, 139, '2025-10-29', 'Presente', 'ok'),
(141, 140, '2025-10-29', 'Presente', 'ok'),
(142, 141, '2025-10-29', 'Presente', 'ok'),
(143, 142, '2025-10-29', 'Presente', 'ok'),
(144, 143, '2025-10-29', 'Presente', 'ok'),
(145, 144, '2025-10-29', 'Presente', 'ok'),
(146, 145, '2025-10-29', 'Presente', 'ok'),
(147, 146, '2025-10-29', 'Presente', 'ok'),
(148, 147, '2025-10-29', 'Presente', 'ok'),
(149, 148, '2025-10-29', 'Presente', 'ok'),
(150, 149, '2025-10-29', 'Presente', 'ok'),
(151, 150, '2025-10-29', 'Presente', 'ok'),
(152, 151, '2025-10-29', 'Presente', 'ok'),
(153, 152, '2025-10-29', 'Presente', 'ok'),
(154, 153, '2025-10-29', 'Presente', 'ok'),
(155, 154, '2025-11-07', 'Ausente', 'se a observado que el estudiante ultimamente a asistido tarde, teniendo faltas constante, se plantea hablar con la familia del estudiante ara llegar a una reflexion !!!');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `curso`
--

CREATE TABLE `curso` (
  `id` int(11) NOT NULL,
  `nombre_curso` varchar(100) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `profesor` varchar(100) DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_fin` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cursos`
--

CREATE TABLE `cursos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `cursos`
--

INSERT INTO `cursos` (`id`, `nombre`) VALUES
(1, '1° Año'),
(2, '2° Año'),
(3, '3° Año'),
(4, '4° Año'),
(5, '5° Año'),
(6, '6° Año');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id_Est` int(11) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `DNI` int(11) NOT NULL,
  `email_Est` varchar(50) NOT NULL,
  `telefono` int(12) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `curso_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id_Est`, `Apellido`, `nombre`, `DNI`, `email_Est`, `telefono`, `fecha_nacimiento`, `curso_id`) VALUES
(1, 'Gondalez', 'Ramiro', 49876567, 'hola@gmail.com', 0, '0000-00-00', 1),
(2, 'Ignacio', 'Chammella', 47912847, '', 0, '0000-00-00', 6),
(3, 'Nahuel', 'Bima', 48537429, '', 0, '0000-00-00', 6),
(4, 'Barbron Mateo', 'Bruno', 48068748, '', 0, '0000-00-00', 6),
(5, 'Dylan', 'Cabera', 48671275, '', 0, '0000-00-00', 6),
(6, 'Laureano', 'Carranza', 48074352, '', 0, '0000-00-00', 6),
(7, 'Centurion Huilen', 'Ceballo', 48601748, '', 0, '0000-00-00', 6),
(8, 'Juan Pablo', 'Dominguez', 48601786, '', 0, '0000-00-00', 6),
(9, 'Ortiz Camila', 'Flores', 48536221, '', 0, '0000-00-00', 6),
(10, 'Valentina', 'Godoy', 48074462, '', 0, '0000-00-00', 6),
(11, 'Amulen', 'Gutierrez', 48601791, '', 0, '0000-00-00', 6),
(12, 'Santino Felipe', 'Hergert', 48820639, '', 0, '0000-00-00', 6),
(13, 'Morena', 'Ledesma', 48130190, '', 0, '0000-00-00', 6),
(14, 'Santiago Nicolas', 'Liendo', 48671247, '', 0, '0000-00-00', 6),
(15, 'Sofia', 'Lugani', 48671239, '', 0, '0000-00-00', 6),
(16, 'Marianela', 'Mattio', 48130105, '', 0, '0000-00-00', 6),
(17, 'Francisco', 'Nuñez', 47912892, '', 0, '0000-00-00', 6),
(18, 'Victorio', 'Paskevicius', 48074409, '', 0, '0000-00-00', 6),
(19, 'Juan Ignacio', 'Pavon', 48130115, '', 0, '0000-00-00', 6),
(20, 'Ignacio Juaquin', 'Restivo', 48719590, '', 0, '0000-00-00', 6),
(21, 'Leonel Andrian', 'Soto', 48537499, '', 0, '0000-00-00', 6),
(22, 'Giuliana', 'Spaccesi', 48074412, '', 0, '0000-00-00', 6),
(23, 'Alvarez Araceli', 'Valfedro', 48671298, '', 0, '0000-00-00', 6),
(24, 'Ana Belen', 'Vergara', 48816879, '', 0, '0000-00-00', 6),
(25, 'Maximo Santiago', 'Bautista', 48239917, '', 0, '0000-00-00', 5),
(26, 'Bruno Gabriel', 'Cabral', 48816872, '', 0, '0000-00-00', 5),
(27, 'Valentino', 'Centeno', 49016488, '', 0, '0000-00-00', 5),
(28, 'Leyla Umma', 'Chiapero', 49384184, '', 0, '0000-00-00', 5),
(29, 'Gianna', 'Colmenares', 48905218, '', 0, '0000-00-00', 5),
(30, 'Gauna Kiara', 'Duran', 49016447, '', 0, '0000-00-00', 5),
(31, 'Tomas', 'Eden', 49288784, '', 0, '0000-00-00', 5),
(32, 'Micael', 'Gimenez', 49500231, '', 0, '0000-00-00', 5),
(33, 'Malena', 'Gomez', 48288756, '', 0, '0000-00-00', 5),
(34, 'Tiago', 'Gomez', 49221251, '', 0, '0000-00-00', 5),
(35, 'Santiago', 'Machado', 49288754, '', 0, '0000-00-00', 5),
(36, 'Paulina', 'Maldonado', 49016478, '', 0, '0000-00-00', 5),
(37, 'Irerra Matias', 'Malissia', 48905206, '', 0, '0000-00-00', 5),
(38, 'Leandro', 'Nuñez', 49016421, '', 0, '0000-00-00', 5),
(39, 'Dylan', 'Oviedo', 51450509, '', 0, '0000-00-00', 5),
(40, 'Nehemias Uriel', 'Ponce', 48074339, '', 0, '0000-00-00', 5),
(41, 'Barco Laura Isabella', 'Quintero', 49794234, '', 0, '0000-00-00', 5),
(42, 'Santiago Nahuel', 'Vigna', 48943297, '', 0, '0000-00-00', 5),
(43, 'Candela', 'Barrionuevo', 50178224, '', 0, '0000-00-00', 4),
(44, 'Martina Aylen', 'Barrionuevo', 49717174, '', 0, '0000-00-00', 4),
(45, 'Sofia Maria Luz', 'Brizuela', 49717176, '', 0, '0000-00-00', 4),
(46, 'Giuvana Alejo', 'Castaño', 50055599, '', 0, '0000-00-00', 4),
(47, 'Mia Brisa', 'Castillo', 49720039, '', 0, '0000-00-00', 4),
(48, 'Gomez Luisana', 'Castillo', 49865028, '', 0, '0000-00-00', 4),
(49, 'Yair', 'Gallay', 48865008, '', 0, '0000-00-00', 4),
(50, 'Kyara Alejandra', 'Gontero', 50178333, '', 0, '0000-00-00', 4),
(51, 'Bautista', 'Grinovero', 49567258, '', 0, '0000-00-00', 4),
(52, 'Kurozaki Alejandro Luis', 'Guevara', 50178293, '', 0, '0000-00-00', 4),
(53, 'Gonzalez Luis Felipe', 'Illarraga', 48720004, '', 0, '0000-00-00', 4),
(54, 'Barrionuevo Franco', 'Lionel', 50090647, '', 0, '0000-00-00', 4),
(55, 'Juaquin', 'Lpoez', 49717197, '', 0, '0000-00-00', 4),
(56, 'Pedro', 'Lujan', 50033574, '', 0, '0000-00-00', 4),
(57, 'Lola', 'Marattin', 48816861, '', 0, '0000-00-00', 4),
(58, 'Malena Guillermina', 'Pino', 49717797, '', 0, '0000-00-00', 4),
(59, 'Juaquin', 'Raffo', 49717205, '', 0, '0000-00-00', 4),
(60, 'Thiago Joel', 'Reinoso', 50090629, '', 0, '0000-00-00', 4),
(61, 'Marco Valentin', 'Romero', 50033545, '', 0, '0000-00-00', 4),
(62, 'Alejo Andres', 'Serminatti', 50238902, '', 0, '0000-00-00', 4),
(63, 'Matias', 'Torres', 49865065, '', 0, '0000-00-00', 4),
(64, 'Sofia Magdalena', 'Vergara', 48865007, '', 0, '0000-00-00', 4),
(65, 'Lucila', 'Zalazar', 50262105, '', 0, '0000-00-00', 4),
(66, 'Morena Jazmín', 'Aguilera', 50634, '', 0, '0000-00-00', 3),
(67, 'Abril', 'Almada', 54023, '', 0, '0000-00-00', 3),
(68, 'Kiara Camila', 'Bagniollueva', 50335, '', 0, '0000-00-00', 3),
(69, 'Sofía Lucrecia –', 'Borghi', 50524, '', 0, '0000-00-00', 3),
(70, 'Gaspar', 'Caballero', 50634, '', 0, '0000-00-00', 3),
(71, 'Abril Milagros', 'Cabral', 50834, '', 0, '0000-00-00', 3),
(72, 'Juan Bautista', 'Caballo', 50528, '', 0, '0000-00-00', 3),
(73, 'Franco Leonel', 'Cejtino', 50923, '', 0, '0000-00-00', 3),
(74, 'Guadalupe', 'Fernández', 50423, '', 0, '0000-00-00', 3),
(75, 'Dalmiro', 'Ferreyra', 50924, '', 0, '0000-00-00', 3),
(76, 'Gerardo Federico', 'Ferreyra', 50924, '', 0, '0000-00-00', 3),
(77, 'Milena', 'Giménez', 50334, '', 0, '0000-00-00', 3),
(78, 'Kiara Abigail', 'Grosso', 50334, '', 0, '0000-00-00', 3),
(79, 'Ema Sofía', 'Gómez', 50423, '', 0, '0000-00-00', 3),
(80, 'Axel Gabriel', 'Gramac', 50824, '', 0, '0000-00-00', 3),
(81, 'Carlos Pablo', 'Juan', 50624, '', 0, '0000-00-00', 3),
(82, 'Pedro Abdul', 'Lleuvo', 50820, '', 0, '0000-00-00', 3),
(83, 'Valentina', 'Ortíz', 50928, '', 0, '0000-00-00', 3),
(84, 'Facundo Agustín', 'Pantilla', 51023, '', 0, '0000-00-00', 3),
(85, 'Morena Jazmín', 'Rodríguez', 51024, '', 0, '0000-00-00', 3),
(86, 'Caeletano Gonzalo Amadeo', 'Ruano', 50334, '', 0, '0000-00-00', 3),
(87, 'Sasha Morena', 'Scalabrini', 51049, '', 0, '0000-00-00', 3),
(88, 'Brian Ezequiel', 'Sosa', 50624, '', 0, '0000-00-00', 3),
(89, 'Kevin Facundo', 'Tomás', 50624, '', 0, '0000-00-00', 3),
(90, 'Thiago Martín', 'Torres', 50923, '', 0, '0000-00-00', 3),
(91, 'Santino', 'Rodríguez', 50835, '', 0, '0000-00-00', 3),
(92, 'González Liz Emilia', 'Núñez', 50835, '', 0, '0000-00-00', 3),
(93, 'Céspedes Brian Adhemar', 'Aguilera', 98537, '', 0, '0000-00-00', 2),
(94, 'Tiziano Javier', 'Barros', 51537, '', 0, '0000-00-00', 2),
(95, 'Barbearol Benjamín', 'Bruno', 51537, '', 0, '0000-00-00', 2),
(96, 'Camila', 'Caliva', 51537, '', 0, '0000-00-00', 2),
(97, 'Tomás Benjamín', 'Canela', 51537, '', 0, '0000-00-00', 2),
(98, 'Maitand Sol', 'Colmenares', 98537, '', 0, '0000-00-00', 2),
(99, 'Emilia', 'Delavega', 51537, '', 0, '0000-00-00', 2),
(100, 'Leonel Benjamín', 'Godoy', 51537, '', 0, '0000-00-00', 2),
(101, 'Hermida Santiago', 'Godoy', 51537, '', 0, '0000-00-00', 2),
(102, 'Mía Victoria', 'Gómez', 51537, '', 0, '0000-00-00', 2),
(103, 'Juan Esteban', 'Gómez', 51537, '', 0, '0000-00-00', 2),
(104, 'Ramiro Ezequiel', 'Gómez', 51537, '', 0, '0000-00-00', 2),
(105, 'Joaquín', 'González', 51537, '', 0, '0000-00-00', 2),
(106, 'Jonathán Joel', 'González', 51537, '', 0, '0000-00-00', 2),
(107, 'Lucas Thiago', 'González', 51537, '', 0, '0000-00-00', 2),
(108, 'Pescatori Ulises', 'Herrera', 51537, '', 0, '0000-00-00', 2),
(109, 'del Sol Axel', 'Iberna', 51537, '', 0, '0000-00-00', 2),
(110, 'Alma', 'Ledesma', 51537, '', 0, '0000-00-00', 2),
(111, 'Ignacio', 'MaldonadoJuan', 51537, '', 0, '0000-00-00', 2),
(112, 'Roberto Miguel', 'Maldonado', 51537, '', 0, '0000-00-00', 2),
(113, 'Emma', 'Palombarini', 51537, '', 0, '0000-00-00', 2),
(114, 'Mathilde Geraldine', 'Pito', 51537, '', 0, '0000-00-00', 2),
(115, 'Facundo Nahuel', 'Reynoso', 52111, '', 0, '0000-00-00', 2),
(116, 'Franco Emiliano', 'Reynoso', 52111, '', 0, '0000-00-00', 2),
(117, 'Esmeralda', 'Romero', 52204, '', 0, '0000-00-00', 2),
(118, 'Fernández Octavio', 'Sequera', 52537, '', 0, '0000-00-00', 2),
(119, 'Zoe Micaela', 'Soria', 52537, '', 0, '0000-00-00', 2),
(120, 'Gonzalo Daniel', 'Sparacino', 52204, '', 0, '0000-00-00', 2),
(121, 'Franco Damián', 'Vergara', 51348, '', 0, '0000-00-00', 2),
(122, 'Antonella Francesca', 'Vigna', 57621, '', 0, '0000-00-00', 2),
(123, 'Francisca Geraldine', 'Almada', 52689, '', 0, '0000-00-00', 1),
(124, 'Aylén', 'Auscar', 52689, '', 0, '0000-00-00', 1),
(125, 'Santino', 'Cardoso', 52689, '', 0, '0000-00-00', 1),
(126, 'Paulina', 'Caminaga', 52689, '', 0, '0000-00-00', 1),
(127, 'Antonio Felipe', 'Ceballos', 52689, '', 0, '0000-00-00', 1),
(128, 'Benjamín Matías', 'Costamagna', 52689, '', 0, '0000-00-00', 1),
(129, 'Roca Bruno Elías', 'Díaz', 52745, '', 0, '0000-00-00', 1),
(130, 'Jerónimo', 'Echarry', 52687, '', 0, '0000-00-00', 1),
(131, 'Benicio', 'Fernández', 52689, '', 0, '0000-00-00', 1),
(132, 'Thiago Daniel', 'Gotogechi', 52689, '', 0, '0000-00-00', 1),
(133, 'Ambar', 'Gomez', 52689, '', 0, '0000-00-00', 1),
(134, 'Elías Javier', 'Gomez', 52689, '', 0, '0000-00-00', 1),
(135, 'Thiago', 'Gomez', 52689, '', 0, '0000-00-00', 1),
(136, 'Abril', 'Guitart', 52689, '', 0, '0000-00-00', 1),
(137, 'Fabrizio', 'Koleszar', 52689, '', 0, '0000-00-00', 1),
(138, 'Lescano Juan Pablo', 'Marin', 52689, '', 0, '0000-00-00', 1),
(139, 'Emanuel', 'Mastrelli', 52689, '', 0, '0000-00-00', 1),
(140, 'Stefano', 'Benjamín', 52689, '', 0, '0000-00-00', 1),
(141, 'Ciro Valentín', 'Moya', 52689, '', 0, '0000-00-00', 1),
(142, 'Farias Francis', 'Ostemeijer', 52689, '', 0, '0000-00-00', 1),
(143, 'Yaco Daniel', 'Páez', 52689, '', 0, '0000-00-00', 1),
(144, 'Lola Valentina', 'Palma', 52689, '', 0, '0000-00-00', 1),
(145, 'Valentina Mar Sol', 'Ramos', 52689, '', 0, '0000-00-00', 1),
(146, 'Francisca Alexia', 'Ramírez', 52689, '', 0, '0000-00-00', 1),
(147, 'Serna Margarita', 'Ruano', 52494, '', 0, '0000-00-00', 1),
(148, 'Pilar Celeste', 'Saiza', 52689, '', 0, '0000-00-00', 1),
(149, 'Ian Itiel', 'Sosa', 52689, '', 0, '0000-00-00', 1),
(150, 'Gaulán Benicio', 'Torres', 52689, '', 0, '0000-00-00', 1),
(151, 'Thiago Gastón', 'Torres', 52689, '', 0, '0000-00-00', 1),
(152, 'Luciano Javier', 'Casali', 52689, '', 0, '0000-00-00', 1),
(153, 'Martín', 'Boschela', 52689, '', 0, '0000-00-00', 1),
(154, 'Ignacio', 'Emmanuel', 47912867, '', 0, '0000-00-00', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `email`, `password`, `fecha_registro`) VALUES
(1, 'Francisco Nuñez', 'rfrichard07@gmail.com', 'scrypt:32768:8:1$gPIsyDa6BES63EPd$5b119db9d40488934343f22a904fa34eb31c95f3f8fcc072175fa952d1b6f1250a9bb7c859de4d14d2804abdb790b3adab21a5472618d5ce12b15eb685fd8f07', '2025-09-23 18:14:36'),
(3, 'Viviana', 'vaguillen@escuelasproa.edu.ar', 'scrypt:32768:8:1$BVyewvyXAQE6FgJt$b66de75863b8fa2073675142c184041fb1ea7507b248004d692ce6bee5033725032e1874001fab947789fa2685505c840b3d7901853248579da1b7499f4875a3', '2025-10-27 11:49:06');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD PRIMARY KEY (`id`),
  ADD KEY `estudiante_id` (`estudiante_id`);

--
-- Indices de la tabla `cursos`
--
ALTER TABLE `cursos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id_Est`),
  ADD KEY `curso_id` (`curso_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asistencias`
--
ALTER TABLE `asistencias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=156;

--
-- AUTO_INCREMENT de la tabla `cursos`
--
ALTER TABLE `cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id_Est` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asistencias`
--
ALTER TABLE `asistencias`
  ADD CONSTRAINT `asistencias_ibfk_1` FOREIGN KEY (`estudiante_id`) REFERENCES `estudiantes` (`id_Est`) ON DELETE CASCADE;

--
-- Filtros para la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD CONSTRAINT `estudiantes_ibfk_1` FOREIGN KEY (`curso_id`) REFERENCES `cursos` (`id`) ON DELETE SET NULL;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
