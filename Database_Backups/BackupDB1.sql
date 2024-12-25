-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: company
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `cliente_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `edad` varchar(100) NOT NULL,
  `telefono` varchar(40) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `ciudad` varchar(50) NOT NULL,
  `direccion` varchar(500) NOT NULL,
  `fecha_registro` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cliente_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,'Carlos Andres Puerto Carreño','21','(+57) 254-587-4587','carlos@gmail.com','Cali','Calle 32A Bis #99-85','2024-10-15 15:27:46'),(2,'Anidez Ricardo Perez Guzman','19','(+57) 314-458-7458','rojovivo@outlook.es','Bogotá','Carrera 26 #66-54B','2024-10-15 22:15:29'),(3,'Laura Manuela Sanchez correal','23','(+1) 354-584-2221','juan.13jsg@gmai.cim','Cali','carrera 23 #69-84B apto 201','2024-10-15 22:30:50'),(4,'Camila Andrea Parra Gutty','14','(+1) 487-854-7448','camilin14@yahoo.com','Florida','1234 Pineapple St, Miami, FL 33101','2024-10-18 18:29:59'),(5,'Jose Duarte Monroy Query','32','(+21) 322-557-8844','perezCheco@yahoo.com','Medellin','calle 4a Diagonal C #25-24','2024-10-29 00:52:12'),(6,'Andrea Tatiana del perpetuo Socorro','11','(+54) 655-255-2254','pezcuso13@gmail.com','Neiva','Calle 23 #43a sur - 34 Noroeste','2024-11-03 21:40:00'),(7,'Diana Manrique','23','(+1) 458-525-2255  ','sdfsdf@gmail.esom','Montería','Calle 4a #23-13','2024-11-04 09:06:35'),(8,'Manuel Enrique Perdomo','23','(+57) 322-544-5552','pepegrillo@gmail.com','Neiva','Av Chile 12B bis #84-75','2024-11-04 09:10:54');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `producto_id` int NOT NULL AUTO_INCREMENT,
  `tipo_producto` int NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `precio` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`producto_id`),
  KEY `fk_producto_tipoProducto` (`tipo_producto`),
  CONSTRAINT `fk_producto_tipoProducto` FOREIGN KEY (`tipo_producto`) REFERENCES `tipo_producto` (`tipo_producto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,1,'Chocolatina Negra',3.000),(2,1,'Chocolate',7.500),(3,1,'Gomitas de fruta',4.300),(4,1,'Caramelo',3.000),(5,1,'Paleta de fresa',3.000),(6,1,'Barra de chocolate',4.000),(7,1,'Chicles de menta',500.000),(8,1,'Galletas rellenas',4.000),(9,1,'Brownie de chocolate',6.000),(10,1,'Tarta de crema',7.000),(11,1,'Bombones de avellana',9.000),(12,2,'Mantequilla',4.500),(13,2,'Aceite de oliva',7.990),(14,2,'Margarina',3.750),(15,2,'Aceite de coco',8.250),(16,2,'Grasa de cerdo',5.300),(17,2,'Aceite vegetal',6.000),(18,2,'Mayonesa',3.990),(19,2,'Aderezo ranch',4.750),(20,2,'Salsa de queso',5.500),(21,2,'Crema agria',3.250),(22,3,'Manzana',1.200),(23,3,'Banana',0.990),(24,3,'Naranja',1.500),(25,3,'Fresas',3.750),(26,3,'Uvas',4.500),(27,3,'Mango',2.990),(28,3,'Piña',3.250),(29,3,'Papaya',2.750),(30,3,'Sandía',5.000),(31,3,'Melocotón',4.000),(32,4,'Lechuga',1.500),(33,4,'Tomate',2.000),(34,4,'Zanahoria',1.200),(35,4,'Cebolla',1.750),(36,4,'Brócoli',2.500),(37,4,'Espinaca',2.990),(38,4,'Pepino',1.300),(39,4,'Coliflor',3.000),(40,4,'Pimiento',2.800),(41,4,'Calabacín',1.900),(42,5,'Carne de res',12.500),(43,5,'Pechuga de pollo',8.990),(44,5,'Carne de cerdo',10.750),(45,5,'Filete de pescado',15.000),(46,5,'Costillas de cerdo',14.250),(47,5,'Chuleta de cordero',18.500),(48,5,'Salchichas',6.500),(49,5,'Tocino',5.750),(50,5,'Carne molida',9.300),(51,5,'Jamón',7.250),(52,6,'Leche',1.500),(53,6,'Yogur',2.250),(54,6,'Queso cheddar',4.000),(55,6,'Mantequilla',3.500),(56,6,'Crema',2.990),(57,6,'Leche condensada',3.750),(58,6,'Queso fresco',3.000),(59,6,'Suero',2.800),(60,6,'Helado',5.500),(61,6,'Nata',4.250),(62,7,'Agua mineral',1.000),(63,7,'Refresco',1.500),(64,7,'Jugo de naranja',2.000),(65,7,'Cerveza',3.500),(66,7,'Vino tinto',10.000),(67,7,'Cerveza artesanal',5.000),(68,7,'Té helado',2.250),(69,7,'Leche de almendras',3.000),(70,7,'Limonada',1.750),(71,7,'Batido de frutas',4.500),(72,8,'Frijoles',2.000),(73,8,'Lentejas',1.800),(74,8,'Garbanzos',2.500),(75,8,'Judías verdes',3.000),(76,8,'Alubias',2.250),(77,8,'Soja',2.750),(78,8,'Guisantes',1.500),(79,8,'Habichuelas',2.100),(80,8,'Lentejas rojas',1.900),(81,8,'Frijoles negros',2.300),(82,9,'Arroz',1.500),(83,9,'Avena',2.000),(84,9,'Trigo',1.800),(85,9,'Cebada',2.250),(86,9,'Maíz',1.600),(87,9,'Quinoa',3.000),(88,9,'Sémola',2.100),(89,9,'Cereal de desayuno',3.500),(90,9,'Harina de trigo',1.750),(91,9,'Mijo',2.800);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_producto`
--

DROP TABLE IF EXISTS `tipo_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_producto` (
  `tipo_producto_id` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`tipo_producto_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_producto`
--

LOCK TABLES `tipo_producto` WRITE;
/*!40000 ALTER TABLE `tipo_producto` DISABLE KEYS */;
INSERT INTO `tipo_producto` VALUES (1,'dulces'),(2,'grasas'),(3,'frutas'),(4,'vegetales'),(5,'carnes'),(6,'lacteos'),(7,'bebidas'),(8,'legumbres'),(9,'cereales');
/*!40000 ALTER TABLE `tipo_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `venta_id` int NOT NULL AUTO_INCREMENT,
  `cliente_id` int NOT NULL,
  `cantidad` int NOT NULL,
  PRIMARY KEY (`venta_id`),
  KEY `fk_cliente_id` (`cliente_id`),
  CONSTRAINT `fk_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente` (`cliente_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (1,1,12),(2,1,13),(3,1,122),(4,1,450),(5,1,13),(6,1,4),(7,2,9),(8,2,320),(9,3,5),(10,3,12),(11,5,60),(12,1,2);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta_producto`
--

DROP TABLE IF EXISTS `venta_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta_producto` (
  `venta_producto_id` int NOT NULL AUTO_INCREMENT,
  `venta_id` int NOT NULL,
  `producto_id` int NOT NULL,
  PRIMARY KEY (`venta_producto_id`),
  UNIQUE KEY `venta_id` (`venta_id`,`producto_id`),
  KEY `fk_ventaProducto_producto_id` (`producto_id`),
  CONSTRAINT `fk_ventaProducto_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `producto` (`producto_id`),
  CONSTRAINT `fk_ventaProducto_venta_id` FOREIGN KEY (`venta_id`) REFERENCES `venta` (`venta_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta_producto`
--

LOCK TABLES `venta_producto` WRITE;
/*!40000 ALTER TABLE `venta_producto` DISABLE KEYS */;
INSERT INTO `venta_producto` VALUES (1,1,1),(2,2,3),(3,3,11),(6,4,12),(7,5,31),(8,6,67),(9,7,69),(10,8,44),(11,9,33),(12,10,26),(13,11,60),(14,12,46);
/*!40000 ALTER TABLE `venta_producto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-24 20:39:07
