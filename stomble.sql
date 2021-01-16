-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2021 at 06:57 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stomble`
--

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `ID` int(100) NOT NULL,
  `city_name` varchar(100) NOT NULL,
  `planet_name` varchar(100) NOT NULL,
  `capacity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`ID`, `city_name`, `planet_name`, `capacity`) VALUES
(0, 'Hello', 'Mars', 2),
(1, 'Sydney', 'Earth', 4),
(3, 'New York', 'Pluto', 2),
(5, 'Melbourne', 'Earth', 1),
(6, 'Isl', 'earth', 1),
(7, 'Lahore', 'Earth', 2),
(8, 'Los Angelas', 'Moon', 1),
(10, 'Area 59', 'Earth', 0);

-- --------------------------------------------------------

--
-- Table structure for table `spaceship`
--

CREATE TABLE `spaceship` (
  `SPACEID` int(11) NOT NULL,
  `LOCATIONID` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `status` enum('decommissioned','maintenance','operational') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `spaceship`
--

INSERT INTO `spaceship` (`SPACEID`, `LOCATIONID`, `name`, `model`, `status`) VALUES
(1, 8, 'Trainover', '2017', 'operational'),
(3, 5, 'G16', '2019', 'decommissioned'),
(4, 6, 'Honda', '2019', 'operational'),
(7, 1, 'Stomble', '2009', 'maintenance');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_user`
--

CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL,
  `user_name` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_email` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `tbl_user`
--

INSERT INTO `tbl_user` (`user_id`, `user_name`, `user_email`, `user_password`) VALUES
(1, 'Soumitra Roy Sarkar', 'contact@roytuts.com', 'pbkdf2:sha256:50000$obX7AAZv$61ba4f743eff5113433a3fd249896deed4120e9a83deaf166477ca5fb74fcd49'),
(2, 'Aston rivers', 'lebron@lakers.com', 'pbkdf2:sha256:150000$swx4M25N$5a9a830e0e5dae2428f56ae58c238bd2df7e8938e7cbe401adaf13000b2769d9');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD UNIQUE KEY `ID` (`ID`);

--
-- Indexes for table `spaceship`
--
ALTER TABLE `spaceship`
  ADD PRIMARY KEY (`SPACEID`),
  ADD KEY `LOCATIONID` (`LOCATIONID`);

--
-- Indexes for table `tbl_user`
--
ALTER TABLE `tbl_user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tbl_user`
--
ALTER TABLE `tbl_user`
  MODIFY `user_id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `spaceship`
--
ALTER TABLE `spaceship`
  ADD CONSTRAINT `spaceship_ibfk_1` FOREIGN KEY (`LOCATIONID`) REFERENCES `locations` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
