-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 24 Des 2024 pada 18.23
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tokotopup`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_transaksi`
--

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int(11) NOT NULL,
  `jproduk` varchar(255) NOT NULL,
  `userId` int(25) NOT NULL,
  `item` varchar(255) NOT NULL,
  `price` varchar(255) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `metode` enum('GoPay','OVO','DANA','ShopeePay') NOT NULL,
  `status` enum('Konfirmasi','Proses','Selesai') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tb_transaksi`
--

INSERT INTO `tb_transaksi` (`id_transaksi`, `jproduk`, `userId`, `item`, `price`, `jumlah`, `email`, `metode`, `status`) VALUES
(11, 'Free Fire', 12345544, '80 Diamonds', 'Rp11.300', 1, 'rizkysyaikek1310@gmail.com', 'DANA', 'Konfirmasi'),
(12, 'Mobile Legends', 23883727, 'Starlight', 'Rp44.000', 1, 'rizzns540@gmail.com', 'GoPay', 'Konfirmasi'),
(13, 'Valorant', 21212144, '1000 Valorant Points', 'Rp100.600', 1, 'rizzns540@gmail.com', 'ShopeePay', 'Konfirmasi'),
(14, 'Call of Dutty', 232345, '3564 CP', 'Rp485.000', 3, 'rizkysyaikek1310@gmail.com', 'OVO', 'Selesai'),
(15, 'PUBG', 2328392, '8100 UC', 'Rp1.450.000', 1, 'rizzns540@gmail.com', 'DANA', 'Selesai'),
(16, 'Genshin Impact', 63676281, '6480+1600 Genesis Crystals', 'Rp1.260.400', 5, 'rizkynursetiawan@students.amikom.ac.id', 'DANA', 'Proses');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tb_users`
--

CREATE TABLE `tb_users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('User','Admin') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `tb_users`
--

INSERT INTO `tb_users` (`id`, `username`, `email`, `password`, `level`) VALUES
(6, 'Admin', 'admin@gmail.com', 'scrypt:32768:8:1$ey2Q4YZR0Yts0vs9$02b569b008a61f53eec6c1f7f0604abcb3c52ba694bea5e716b6f97bdd64627286a92a1a97e58097342828dbd8fc807acb736d5cc8ce11444e3ec2bff9d636b4', 'Admin'),
(7, 'maman', 'maman@gmail.com', 'scrypt:32768:8:1$mi6eyPaobdKVmLXb$99cf3ad0cd362053cb8b5e2901fec458866236d770c13cb50e86567ded99f3960ad35dd09bb95a5b7a244bbf81ff6fb1e85112890b9314fa2089e4df7bccce7b', 'User'),
(8, 'agus', 'agus@gmail.com', 'scrypt:32768:8:1$558T8C99YL9LrzIT$57c956fa7a731da53eb4cf25b63fc71fd9332c3d9afd22d9d0e5e851de5b384e362493513a966cf52540712c03309cd6a68983abb97c5faf7b6757899cdcf48a', 'User'),
(10, 'admin2', 'admin2@gmail.com', 'scrypt:32768:8:1$FKZ0ICiaEQt6BypC$fc7b4b301340c01207df67112ec3acd70b984faaa7248c3f124dfe5b1fc6ea5d5f42d5489504d03c9b51d4c587e66936765c2b4749ddda2d5a1920e2f53603f5', 'Admin');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  ADD PRIMARY KEY (`id_transaksi`);

--
-- Indeks untuk tabel `tb_users`
--
ALTER TABLE `tb_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `tb_transaksi`
--
ALTER TABLE `tb_transaksi`
  MODIFY `id_transaksi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT untuk tabel `tb_users`
--
ALTER TABLE `tb_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
