-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2019 at 08:28 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` text DEFAULT NULL,
  `password` text DEFAULT NULL,
  `token` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `password`, `token`) VALUES
(1, 'dahlia', '123', NULL),
(2, 'dahlia', '123', NULL),
(3, 'dahlia', '123', 'None'),
(4, 'dahlia', '123', NULL),
(5, 'dahlia', '123', NULL),
(6, 'dahlia', '123', NULL),
(7, 'dahlia', '123', NULL),
(8, 'dahlia', '123', NULL),
(9, 'dahlia', '123', NULL),
(10, 'dahlia', '123', NULL),
(11, 'dahlia', '123', NULL),
(12, 'dahlia', '123', NULL),
(13, 'dahlia', '123', NULL),
(14, 'dahlia', '123', NULL),
(15, 'dahlia', '123', NULL),
(16, 'dahlia', '123', NULL),
(17, 'dahlia', '123', '123'),
(18, 'dahlia', '123', NULL),
(19, 'dahlia', '123', 'None'),
(20, 'dahlia', '123', NULL),
(21, 'dahlia', '123', NULL),
(22, 'dahlia', '123', NULL),
(23, 'dahlia', '123', NULL),
(24, 'dahlia', '123', NULL),
(25, 'dahlia', '123', NULL),
(26, 'dahlia', '123', NULL),
(27, 'dahlia', '123', NULL),
(28, 'dahlia', '123', NULL),
(29, 'dahlia', '123', NULL),
(30, 'dahlia', '123', '3a0WGv9xk0'),
(31, 'dahlia', '123', 'emFAlKIIBB'),
(32, 'dahlia', '123', 'bGNGfVuwRr'),
(33, 'dahlia', '123', 'UjJx2gRjpY'),
(34, 'dahlia', '123', 'ONePBz14BR'),
(35, 'dahlia', '123', 'bM3BySog5S'),
(36, 'dahlia', '123', 'YPJjH8StaX'),
(37, 'dahlia', '123', 'uzAbVWJ2CR'),
(38, 'dahlia', '123', 'o7xfZCaIKv'),
(39, 'dahlia', '123', '7Oq9GfEyTP'),
(40, 'dahlia', '123', '8acOR9wuKs');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
