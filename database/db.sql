-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.33 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para parcial_3
CREATE DATABASE IF NOT EXISTS `parcial_3` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `parcial_3`;

-- Volcando estructura para tabla parcial_3.acortador
CREATE TABLE IF NOT EXISTS `acortador` (
  `id_acortador` bigint(20) NOT NULL AUTO_INCREMENT,
  `short_url` varchar(50) DEFAULT NULL,
  `large_url` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id_acortador`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial_3.acortador: ~0 rows (aproximadamente)
DELETE FROM `acortador`;
/*!40000 ALTER TABLE `acortador` DISABLE KEYS */;
INSERT INTO `acortador` (`id_acortador`, `short_url`, `large_url`) VALUES
	(1, 'http://127.0.0.1:5000/YYZ', 'https://www.scribd.com/document/438920790/OPTIMIZACION-docx');
/*!40000 ALTER TABLE `acortador` ENABLE KEYS */;

-- Volcando estructura para tabla parcial_3.archivos
CREATE TABLE IF NOT EXISTS `archivos` (
  `id_archivo` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_usuario` bigint(20) DEFAULT NULL,
  `nombre_archivo` varchar(255) DEFAULT NULL,
  `ruta_archivo` varchar(500) DEFAULT NULL,
  `ruta_vista` varchar(500) DEFAULT NULL,
  `type` varchar(500) DEFAULT NULL,
  `size` varchar(20) DEFAULT NULL,
  `accesso` varchar(3) DEFAULT NULL,
  `url_share` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_archivo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial_3.archivos: ~0 rows (aproximadamente)
DELETE FROM `archivos`;
/*!40000 ALTER TABLE `archivos` DISABLE KEYS */;
/*!40000 ALTER TABLE `archivos` ENABLE KEYS */;

-- Volcando estructura para tabla parcial_3.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id_usuario` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(50) DEFAULT NULL,
  `apellido_usuario` varchar(255) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `validate` varchar(5) DEFAULT NULL,
  `url_val_mail` varchar(100) DEFAULT NULL,
  `url_pass` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla parcial_3.usuarios: ~0 rows (aproximadamente)
DELETE FROM `usuarios`;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
