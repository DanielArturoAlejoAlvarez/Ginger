-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 23, 2020 at 09:35 AM
-- Server version: 5.7.32-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-29+ubuntu16.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ginger_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `todo`
--

CREATE TABLE `todo` (
  `id` int(11) NOT NULL,
  `content` varchar(512) DEFAULT NULL,
  `done` tinyint(1) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `todo`
--

INSERT INTO `todo` (`id`, `content`, `done`, `user_id`) VALUES
(1, 'I have to create a web application using Ruby on Rails.', 0, 1),
(2, 'I have to terminate the mobile application using android studio and Kotlin.', 0, 1),
(3, 'I must create a professional Logo for my brand in my portfolio.', 0, 1),
(4, 'I must build an Rest Api for my shopping cart with Django framework.', 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `public_id` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(128) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `avatar` varchar(512) DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `public_id`, `name`, `email`, `username`, `password`, `avatar`, `admin`) VALUES
(1, '0a81e2d5-72fe-46ec-ab14-ce4243732aa0', 'Caspar Lee', 'casplee@yahoo.com', 'casplee', 'sha256$tlvkfn2Y$e6dc6f737f60f04f9952bb78dc5c046b8738d47c78142334a62c6e252b51a425', 'https://yt3.ggpht.com/ytc/AAUvwngJah2f5yH0GnVL9vcNIuhS7P-i-JGk6zK66P9N8A=s900-c-k-c0x00ffffff-no-rj', 1),
(2, 'dbd9a35e-fc18-499d-a0f3-ff0f426ffbc4', 'Zoe Sugg', 'zoesugg@gmail.com', 'zoesugg', 'sha256$DSnjFACi$d140c8216053ce7e93f36996fa1fb0e6b03f2e0eb82e8dee18d0d8204fbc3e7e', 'https://story.storiesdb.ch/1404208/profile_pic.jpg', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `todo`
--
ALTER TABLE `todo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `public_id` (`public_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `todo`
--
ALTER TABLE `todo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
