-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: FosslipyDB
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Free_Workshop`
--

DROP TABLE IF EXISTS `Free_Workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Free_Workshop` (
  `F_id` int(11) NOT NULL AUTO_INCREMENT,
  `College_Name` varchar(40) DEFAULT NULL,
  `Location` varchar(40) DEFAULT NULL,
  `HOD_Name` varchar(40) DEFAULT NULL,
  `Contact_Details` varchar(11) DEFAULT NULL,
  `Seminar_Date` date DEFAULT NULL,
  `Topic` varchar(40) DEFAULT NULL,
  `Expectation` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`F_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Free_Workshop`
--

LOCK TABLES `Free_Workshop` WRITE;
/*!40000 ALTER TABLE `Free_Workshop` DISABLE KEYS */;
INSERT INTO `Free_Workshop` VALUES (2,'chetana','fjfj','fdg','7303099677','0005-05-05','ffg','fjh');
/*!40000 ALTER TABLE `Free_Workshop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Paid_Workshop`
--

DROP TABLE IF EXISTS `Paid_Workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Paid_Workshop` (
  `P_id` int(11) NOT NULL AUTO_INCREMENT,
  `College_Name` varchar(40) DEFAULT NULL,
  `Location` varchar(40) DEFAULT NULL,
  `HOD_Name` varchar(40) DEFAULT NULL,
  `Contact_Details` varchar(11) DEFAULT NULL,
  `Seminar_Date` date DEFAULT NULL,
  `Topic` varchar(40) DEFAULT NULL,
  `Remark` varchar(100) DEFAULT NULL,
  `U_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`P_id`),
  KEY `U_id` (`U_id`),
  CONSTRAINT `Paid_Workshop_ibfk_1` FOREIGN KEY (`U_id`) REFERENCES `Upcoming_Workshop` (`U_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paid_Workshop`
--

LOCK TABLES `Paid_Workshop` WRITE;
/*!40000 ALTER TABLE `Paid_Workshop` DISABLE KEYS */;
INSERT INTO `Paid_Workshop` VALUES (2,'shreyas','parel','chetan','689463946','0006-06-06','jdl','hello',NULL),(3,'shreyas','bandra','mak','689463946','0006-06-06','jdl','welcomme to bandra',NULL);
/*!40000 ALTER TABLE `Paid_Workshop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Registration`
--

DROP TABLE IF EXISTS `Registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Registration` (
  `User_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(40) DEFAULT NULL,
  `Username` varchar(40) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`User_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Registration`
--

LOCK TABLES `Registration` WRITE;
/*!40000 ALTER TABLE `Registration` DISABLE KEYS */;
INSERT INTO `Registration` VALUES (1,'shreyas pawar','shreyaspawar91@gmail.com','shrey1234'),(2,'shreyas pawar','shreyaspawar91@gmail.com','shrey1234'),(3,'shreyas pawar','shreyaspawar91@gmail.com','shrey1234'),(4,'shreyas pawar','shreyaspawar91@gmail.com','shrey1234'),(5,'shreyas pawar','shreyaspawar91@gmail.com','shrey1234'),(6,'shreyas pawar','shreyaspawar91@gmail.com','shrey1234'),(7,'shreyas pawar','shreyaspawar91@gmail.com','shrey1234'),(8,'abcd','abc@gmail.com','abc'),(9,'chetan','chetan@gmail.com','chetan'),(10,'shreyas','shrey@gmail.com','shreyas'),(11,'shreyas','shrey@gmail.com','shreyas');
/*!40000 ALTER TABLE `Registration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Upcoming_Workshop`
--

DROP TABLE IF EXISTS `Upcoming_Workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Upcoming_Workshop` (
  `U_id` int(11) NOT NULL AUTO_INCREMENT,
  `College_Name` varchar(40) DEFAULT NULL,
  `Location` varchar(40) DEFAULT NULL,
  `HOD_Name` varchar(40) DEFAULT NULL,
  `Contact_Details` varchar(11) DEFAULT NULL,
  `Seminar_Date` date DEFAULT NULL,
  `Topic` varchar(40) DEFAULT NULL,
  `Approach_Date` date DEFAULT NULL,
  `Follow_up1` varchar(100) DEFAULT NULL,
  `Follow_up2` varchar(100) DEFAULT NULL,
  `Follow_up3` varchar(100) DEFAULT NULL,
  `F_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`U_id`),
  KEY `F_id` (`F_id`),
  CONSTRAINT `Upcoming_Workshop_ibfk_1` FOREIGN KEY (`F_id`) REFERENCES `Free_Workshop` (`F_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Upcoming_Workshop`
--

LOCK TABLES `Upcoming_Workshop` WRITE;
/*!40000 ALTER TABLE `Upcoming_Workshop` DISABLE KEYS */;
INSERT INTO `Upcoming_Workshop` VALUES (3,'shreyas pawar','bandra','chetan','689463946','0006-06-06','jdl','0007-07-07','dnlj','nfss','scn',NULL),(5,'chetana','ghatkopar','chetan','689463946','0006-06-06','jdl','0007-07-07','dnlj','nfss','scn',NULL),(6,'chetana rj','ghatkopar','chetan','689463946','0006-06-06','jdl','0007-07-07','dnlj','nfss','scn',NULL),(7,'rj','ghatkopar','chetan','78478','0005-05-05','hii','0006-06-06','hello','hello','hello',NULL);
/*!40000 ALTER TABLE `Upcoming_Workshop` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-27 17:38:32
