-- phpMyAdmin SQL Dump
-- version 3.5.5
-- http://www.phpmyadmin.net
--
-- Host: sql3.freemysqlhosting.net
-- Generation Time: Oct 14, 2014 at 09:38 PM
-- Server version: 5.5.35-0ubuntu0.12.04.2
-- PHP Version: 5.3.28

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `sql354178`
--

-- --------------------------------------------------------

--
-- Table structure for table `Manager`
--

CREATE TABLE IF NOT EXISTS `Manager` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Age` varchar(255) DEFAULT NULL,
  `Company` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Name` (`Name`,`Company`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `Manager`
--

INSERT INTO `Manager` (`ID`, `Name`, `Age`, `Company`) VALUES
(1, 'Jack', '21', 'TATA'),
(2, 'James', '25', 'TATA'),
(3, 'Ron', '35', 'Apple'),
(4, 'Hiten', '29', 'Nix'),
(5, 'Suzen', '38', 'Parle');

-- --------------------------------------------------------

--
-- Table structure for table `manages`
--

CREATE TABLE IF NOT EXISTS `manages` (
  `Type1` varchar(255) NOT NULL DEFAULT '',
  `id1` int(11) NOT NULL DEFAULT '0',
  `Type2` varchar(255) NOT NULL DEFAULT '',
  `id2` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Type1`,`id1`,`Type2`,`id2`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `manages`
--

INSERT INTO `manages` (`Type1`, `id1`, `Type2`, `id2`) VALUES
('Manager', 1, 'Teacher', 1),
('Manager', 1, 'Teacher', 2),
('Manager', 5, 'Manager', 1);

-- --------------------------------------------------------

--
-- Table structure for table `RELATION`
--

CREATE TABLE IF NOT EXISTS `RELATION` (
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `RELATION`
--

INSERT INTO `RELATION` (`name`) VALUES
('manages'),
('teaches');

-- --------------------------------------------------------

--
-- Table structure for table `Student`
--

CREATE TABLE IF NOT EXISTS `Student` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Age` varchar(255) DEFAULT NULL,
  `School` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Name` (`Name`,`School`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `Student`
--

INSERT INTO `Student` (`ID`, `Name`, `Age`, `School`) VALUES
(1, 'Vatsal', '21', 'SCSE'),
(2, 'Abhishek', '20', 'SCSE'),
(3, 'Jalaj', '20', 'SCSE'),
(4, 'PIYUSH', '20', 'MECH');

-- --------------------------------------------------------

--
-- Table structure for table `Teacher`
--

CREATE TABLE IF NOT EXISTS `Teacher` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Exp` varchar(255) DEFAULT NULL,
  `School` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Name` (`Name`,`Exp`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `Teacher`
--

INSERT INTO `Teacher` (`ID`, `Name`, `Exp`, `School`) VALUES
(1, 'Rahul', '5', 'MECH'),
(2, 'Wyan', '10', 'SCSE'),
(3, 'Arun K', '6', 'SCSE');

-- --------------------------------------------------------

--
-- Table structure for table `teaches`
--

CREATE TABLE IF NOT EXISTS `teaches` (
  `Type1` varchar(255) NOT NULL DEFAULT '',
  `id1` int(11) NOT NULL DEFAULT '0',
  `Type2` varchar(255) NOT NULL DEFAULT '',
  `id2` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Type1`,`id1`,`Type2`,`id2`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teaches`
--

INSERT INTO `teaches` (`Type1`, `id1`, `Type2`, `id2`) VALUES
('Student', 1, 'Student', 4),
('Teacher', 1, 'Student', 1),
('Teacher', 2, 'Student', 1),
('Teacher', 2, 'Student', 4);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
