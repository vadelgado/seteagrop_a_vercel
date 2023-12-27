CREATE DATABASE  IF NOT EXISTS `seteagrop` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `seteagrop`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: seteagrop
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `CategoriaID` int NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  PRIMARY KEY (`CategoriaID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (1,'Perros'),(2,'Gatos'),(3,'Ganadería');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citas_peluqueria`
--

DROP TABLE IF EXISTS `citas_peluqueria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citas_peluqueria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identificacion_dueno` varchar(30) DEFAULT NULL,
  `nombre_mascota` varchar(255) NOT NULL,
  `raza_mascota` varchar(255) DEFAULT NULL,
  `edad_mascota` varchar(255) NOT NULL,
  `servicio_solicitado` varchar(255) NOT NULL,
  `fecha_cita` date NOT NULL,
  `hora_cita` varchar(30) DEFAULT NULL,
  `numero_dueno` varchar(13) NOT NULL,
  `observaciones` text,
  PRIMARY KEY (`id`),
  KEY `identificacion_dueno` (`identificacion_dueno`),
  CONSTRAINT `citas_peluqueria_ibfk_1` FOREIGN KEY (`identificacion_dueno`) REFERENCES `usuarios` (`Identificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citas_peluqueria`
--

LOCK TABLES `citas_peluqueria` WRITE;
/*!40000 ALTER TABLE `citas_peluqueria` DISABLE KEYS */;
INSERT INTO `citas_peluqueria` VALUES (1,'1234567123','pepe','vacuno','5 meses','corte de pelo','2023-11-29','04:30 PM','593997002923','mcmg');
/*!40000 ALTER TABLE `citas_peluqueria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `facturas` (
  `FacturaID` int NOT NULL,
  `UsuarioID` varchar(30) NOT NULL,
  `Fecha` date NOT NULL,
  PRIMARY KEY (`FacturaID`),
  KEY `UsuarioID` (`UsuarioID`),
  CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`UsuarioID`) REFERENCES `usuarios` (`Identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` VALUES (1,'1001001','2023-12-10'),(2,'1001234','2023-12-11'),(3,'123456789','2023-12-12');
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `pid` bigint unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `fk_category` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` text,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `pid` (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (31,'1','Juguete para masticar','imagen1.jpg',1,15.99,'Juguete resistente para perros que les gusta morder.'),(32,'2','Comida premium para perros','imagen2.jpg',1,29.99,'Alimento balanceado y nutritivo para perros de todas las edades.'),(33,'3','Collar ajustable','imagen3.jpg',1,12.50,'Collar cómodo y ajustable para perros de diferentes tamaños.'),(34,'4','Cama acolchada para perros','imagen4.jpg',1,45.99,'Cama suave y cómoda para que tu perro descanse plácidamente.'),(35,'5','Pelota de goma indestructible','imagen5.jpg',1,8.99,'Pelota resistente para juegos interactivos con tu perro.'),(36,'6','Chaleco reflectante para perros','imagen6.jpg',1,19.99,'Chaleco con material reflectante para mayor visibilidad durante paseos nocturnos.'),(37,'7','Snacks saludables para perros','imagen7.jpg',1,7.49,'Snacks nutritivos y deliciosos para premiar a tu perro.'),(38,'8','Shampoo hipoalergénico para perros','imagen8.jpg',1,14.99,'Shampoo suave y sin fragancias fuertes para perros con piel sensible.'),(39,'9','Cepillo de dientes para perros','imagen9.jpg',1,6.50,'Cepillo diseñado para mantener la salud dental de tu perro.'),(40,'10','Transportín para perros pequeños','imagen10.jpg',1,39.99,'Transportín cómodo y seguro para viajar con tu perro.'),(41,'11','Rascador de gatos','imagen11.jpg',2,25.99,'Rascador con juguete incorporado para mantener a tu gato entretenido.'),(42,'12','Arena para gatos','imagen12.jpg',2,12.99,'Arena absorbente para mantener la bandeja de tu gato limpia y fresca.'),(43,'13','Juguetes de peluche para gatos','imagen13.jpg',2,8.99,'Set de juguetes suaves y divertidos para que tu gato juegue.'),(44,'14','Comida gourmet para gatos','imagen14.jpg',2,34.50,'Alimento de alta calidad para gatos exigentes con su paladar.'),(45,'15','Caja de arena autolimpiante','imagen15.jpg',2,79.99,'Caja de arena automática que mantiene la arena limpia sin esfuerzo.'),(46,'16','Túnel de juego para gatos','imagen16.jpg',2,18.75,'Túnel plegable para que tu gato se divierta explorando.'),(47,'17','Bolso transportador para gatos','imagen17.jpg',2,32.99,'Bolso cómodo para llevar a tu gato de manera segura y elegante.'),(48,'18','Snacks naturales para gatos','imagen18.jpg',2,6.99,'Snacks saludables y sabrosos para consentir a tu gato.'),(49,'19','Fuente de agua para gatos','imagen19.jpg',2,28.49,'Fuente que proporciona agua fresca y en movimiento para estimular a tu gato a beber.'),(50,'20','Cama elevada para gatos','imagen20.jpg',2,45.00,'Cama elevada para que tu gato tenga su propio espacio elevado y cómodo.'),(51,'21','Suplemento nutricional para ganado','imagen21.jpg',3,49.99,'Mejora la salud y el rendimiento de tu ganado con este suplemento.'),(52,'22','Vitamina para aves de corral','imagen22.jpg',3,19.99,'Vitamina esencial para el crecimiento y la producción de aves de corral.'),(53,'23','Bloques de sales minerales','imagen23.jpg',3,12.50,'Bloques que proporcionan minerales esenciales para la salud del ganado.'),(54,'24','Cerca eléctrica para pastoreo','imagen24.jpg',3,89.99,'Sistema de cerca eléctrica para mantener al ganado en áreas específicas.'),(55,'25','Comedero automático para ganado','imagen25.jpg',3,55.75,'Comedero que dispensa alimentos automáticamente para facilitar la alimentación del ganado.'),(56,'26','Antiparasitario para ovinos','imagen26.jpg',3,15.99,'Tratamiento para controlar y prevenir parásitos en ovejas y otros ovinos.'),(57,'27','Jaula de transporte para aves','imagen27.jpg',3,38.49,'Jaula resistente y segura para transportar aves de corral.'),(58,'28','Acondicionador de suelos para pasto','imagen28.jpg',3,42.99,'Producto que mejora la calidad del suelo para un pasto más nutritivo.'),(59,'29','Insecticida para ganado','imagen29.jpg',3,27.50,'Insecticida que protege al ganado contra insectos molestos y dañinos.'),(60,'30','Cubierta térmica para terneros','imagen30.jpg',3,65.00,'Cubierta que ayuda a mantener a los terneros cálidos en climas fríos.');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `pid` bigint unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `fk_category` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `description` text,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `pid` (`pid`),
  KEY `fk_category` (`fk_category`),
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`fk_category`) REFERENCES `categorias` (`CategoriaID`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (31,'1','Juguete para masticar','imagen1.jpg',1,15.99,'Juguete resistente para perros que les gusta morder.'),(32,'2','Comida premium para perros','imagen2.jpg',1,29.99,'Alimento balanceado y nutritivo para perros de todas las edades.'),(33,'3','Collar ajustable','imagen3.jpg',1,12.50,'Collar cómodo y ajustable para perros de diferentes tamaños.'),(34,'4','Cama acolchada para perros','imagen4.jpg',1,45.99,'Cama suave y cómoda para que tu perro descanse plácidamente.'),(35,'5','Pelota de goma indestructible','imagen5.jpg',1,8.99,'Pelota resistente para juegos interactivos con tu perro.'),(36,'6','Chaleco reflectante para perros','imagen6.jpg',1,19.99,'Chaleco con material reflectante para mayor visibilidad durante paseos nocturnos.'),(37,'7','Snacks saludables para perros','imagen7.jpg',1,7.49,'Snacks nutritivos y deliciosos para premiar a tu perro.'),(38,'8','Shampoo hipoalergénico para perros','imagen8.jpg',1,14.99,'Shampoo suave y sin fragancias fuertes para perros con piel sensible.'),(39,'9','Cepillo de dientes para perros','imagen9.jpg',1,6.50,'Cepillo diseñado para mantener la salud dental de tu perro.'),(40,'10','Transportín para perros pequeños','imagen10.jpg',1,39.99,'Transportín cómodo y seguro para viajar con tu perro.'),(41,'11','Rascador de gatos','imagen11.jpg',2,25.99,'Rascador con juguete incorporado para mantener a tu gato entretenido.'),(42,'12','Arena para gatos','imagen12.jpg',2,12.99,'Arena absorbente para mantener la bandeja de tu gato limpia y fresca.'),(43,'13','Juguetes de peluche para gatos','imagen13.jpg',2,8.99,'Set de juguetes suaves y divertidos para que tu gato juegue.'),(44,'14','Comida gourmet para gatos','imagen14.jpg',2,34.50,'Alimento de alta calidad para gatos exigentes con su paladar.'),(45,'15','Caja de arena autolimpiante','imagen15.jpg',2,79.99,'Caja de arena automática que mantiene la arena limpia sin esfuerzo.'),(46,'16','Túnel de juego para gatos','imagen16.jpg',2,18.75,'Túnel plegable para que tu gato se divierta explorando.'),(47,'17','Bolso transportador para gatos','imagen17.jpg',2,32.99,'Bolso cómodo para llevar a tu gato de manera segura y elegante.'),(48,'18','Snacks naturales para gatos','imagen18.jpg',2,6.99,'Snacks saludables y sabrosos para consentir a tu gato.'),(49,'19','Fuente de agua para gatos','imagen19.jpg',2,28.49,'Fuente que proporciona agua fresca y en movimiento para estimular a tu gato a beber.'),(50,'20','Cama elevada para gatos','imagen20.jpg',2,45.00,'Cama elevada para que tu gato tenga su propio espacio elevado y cómodo.'),(51,'21','Suplemento nutricional para ganado','imagen21.jpg',3,49.99,'Mejora la salud y el rendimiento de tu ganado con este suplemento.'),(52,'22','Vitamina para aves de corral','imagen22.jpg',3,19.99,'Vitamina esencial para el crecimiento y la producción de aves de corral.'),(53,'23','Bloques de sales minerales','imagen23.jpg',3,12.50,'Bloques que proporcionan minerales esenciales para la salud del ganado.'),(54,'24','Cerca eléctrica para pastoreo','imagen24.jpg',3,89.99,'Sistema de cerca eléctrica para mantener al ganado en áreas específicas.'),(55,'25','Comedero automático para ganado','imagen25.jpg',3,55.75,'Comedero que dispensa alimentos automáticamente para facilitar la alimentación del ganado.'),(56,'26','Antiparasitario para ovinos','imagen26.jpg',3,15.99,'Tratamiento para controlar y prevenir parásitos en ovejas y otros ovinos.'),(57,'27','Jaula de transporte para aves','imagen27.jpg',3,38.49,'Jaula resistente y segura para transportar aves de corral.'),(58,'28','Acondicionador de suelos para pasto','imagen28.jpg',3,42.99,'Producto que mejora la calidad del suelo para un pasto más nutritivo.'),(59,'29','Insecticida para ganado','imagen29.jpg',3,27.50,'Insecticida que protege al ganado contra insectos molestos y dañinos.'),(60,'30','Cubierta térmica para terneros','imagen30.jpg',3,65.00,'Cubierta que ayuda a mantener a los terneros cálidos en climas fríos.');
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `Identificacion` varchar(30) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `Apellido` varchar(50) NOT NULL,
  `Tipo_Identificacion` varchar(50) DEFAULT NULL,
  `Correo` varchar(150) NOT NULL,
  `Password` varchar(255) NOT NULL,
  PRIMARY KEY (`Identificacion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES ('1001001','Victor','Delgado','cedula ciudadania','victor@gmail.com','scrypt:32768:8:1$mS9g6fTuLlrVB6uv$43984cd3c56b5df289bb2f1d2543b035cf88a7bc0746852f59685af696958a3fe6e963c4557aa307cfac119e86fcb57aa999fec11cbff21c04fa76497a081515'),('1001234','Samuel Rosales Garcia','chamorro','cedula ciudadania','samuel@gmail.com','scrypt:32768:8:1$rbhaI10rKW7AQPdg$9d6a3190fe423b4604f9108d60fe159e03b7afb0232d3435659d6e5c777d5ced29dde0c348cc91780216e084ceaabe8063bdd1224876e505d2a3f82a3fd19ae9'),('102301203','juan','Javier','cedula ciudadania','juan@correo.com','scrypt:32768:8:1$vDQ3aM0Dxw3cwxCq$af1f53f9252238f8c1c185f6382f3b22d766a583151f8c82a10c0feb970af370200f442646339a1ac7d315cd6a95c4888f691360c3cadd9f006392422c6b3356'),('1085937260','Angela Carina','Ceron Benavides','cedula de ciudadania','karynaceron@gmail.com','scrypt:32768:8:1$9oJiv8W2Z0gGbADz$ece410ece83dc10e407f165da3b0fd292554a9533c6344f0452eb75021e743f1397408eabe047e928ab09affb896c634b3e70ee524ae060c6b71d8848c93149e'),('1234567','Ramon Jimenez Gonzales','Gonzales','cedula ciudadania','ramon@gmail.com','scrypt:32768:8:1$88kkLYlPGUckfQl3$3075af0810cfd45f5572f8d60b0d7dfcce51556d8744b813f688e4a570fd771418d6f21a9d3c0eaaba921d8e421b24a4c66634cd0599bb384873e9059bac997a'),('1234567123','victor','delgado','cedula ciudadania','victor1@correo.com','scrypt:32768:8:1$1J9j0QNaz9t3dNKI$58a13a864f1dd442ad8ec94b80b940d61690a0f24dcd6d47890f16846ab7f794f10b6f14c232c3750aad2d5c10412a65ce7de23a84e79e09b5ecc74e38221e2e'),('123456789','Maria','Gonzales','cedula extranjeria','mariagonzales@gmail.com','scrypt:32768:8:1$SjRL5CuhtgGMnir3$53dacee915085cc584d639404439b472165b3de0169e5cff83a4478bee238fd72f6135ab33cc412f160cc24dbe827952e893d5a1ccfef9a231817b0d7781d3d1'),('12345686','Maria','Fernandez','cedula extranjeria','maria@gmail.com','scrypt:32768:8:1$qYb2EceOnuFWam5r$224ac939bdf9f3a26931091d6ee7b475548780bf0e5db7f2385dea3134d0870eae4a7d0d3c04d6d4c38b3c0a77cc2ed44f6cb22c99e020743086b51945351025');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinaria`
--

DROP TABLE IF EXISTS `veterinaria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinaria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `identificacion_dueno` varchar(30) NOT NULL,
  `numero_dueno` varchar(13) NOT NULL,
  `nombre_mascota` varchar(255) NOT NULL,
  `especie_mascota` varchar(50) NOT NULL,
  `raza_mascota` varchar(255) DEFAULT NULL,
  `edad_mascota` varchar(255) NOT NULL,
  `peso_mascota` varchar(255) NOT NULL,
  `sexo_mascota` varchar(10) NOT NULL,
  `fecha_cita` date NOT NULL,
  `hora_cita` varchar(30) DEFAULT NULL,
  `razon_cita` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `identificacion_dueno` (`identificacion_dueno`),
  CONSTRAINT `veterinaria_ibfk_1` FOREIGN KEY (`identificacion_dueno`) REFERENCES `usuarios` (`Identificacion`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veterinaria`
--

LOCK TABLES `veterinaria` WRITE;
/*!40000 ALTER TABLE `veterinaria` DISABLE KEYS */;
INSERT INTO `veterinaria` VALUES (1,'1234567123','997002923','lorito','otro','Ave cantora','5 meses','9','macho','2023-11-29','gmcgh','07:30 PM'),(2,'1234567123','3153714604','Peggy','perro','pudle','7 años','2','hembra','2023-11-29','aksjdklasd','08:30 AM'),(3,'1234567123','3203668520','Yiva','hamster','Rusa','1 año y medio','3','macho','2023-11-29','ajaksbd','08:00 AM'),(4,'1234567123','3205687410','pepe','gato','Rusa','1 año y medio','0.5 gramos','macho','2023-11-30','dsfgdf','04:30 PM');
/*!40000 ALTER TABLE `veterinaria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'seteagrop'
--

--
-- Dumping routines for database 'seteagrop'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-03 10:04:40
