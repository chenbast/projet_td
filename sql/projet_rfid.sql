-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 01 avr. 2026 à 16:13
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projet_rfid`
--

-- --------------------------------------------------------

--
-- Structure de la table `detection`
--

CREATE TABLE `detection` (
  `num_detec` int(11) NOT NULL,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  `id_tag` varchar(100) NOT NULL,
  `autorisation` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `detection`
--

INSERT INTO `detection` (`num_detec`, `date`, `heure`, `id_tag`, `autorisation`) VALUES
(2, '2026-03-01', '16:29:40', 'CF946748', 'false'),
(3, '2026-03-03', '03:06:08', 'CF946748', 'false'),
(4, '2026-03-03', '08:33:49', 'CF946748', 'false'),
(5, '2026-03-20', '15:36:19', 'CF946748', 'false'),
(6, '2026-03-20', '15:41:12', 'CF946748', 'true'),
(7, '2026-03-20', '15:41:29', 'CF946748', 'false'),
(9, '2026-03-20', '15:43:43', 'B3F28D1A', 'true'),
(10, '2026-03-20', '15:44:50', 'B3F28D1A', 'true'),
(11, '2026-03-20', '15:47:10', '08403108', 'false'),
(12, '2026-03-20', '15:47:56', '04104792681190', 'false'),
(13, '2026-03-20', '15:48:12', '044DB232CE6180', 'false'),
(14, '2026-03-20', '15:48:35', 'CF8949898516', 'true'),
(15, '2026-03-20', '15:48:38', 'CF8949898516', 'true'),
(16, '2026-03-20', '15:49:50', 'B3F28D1A', 'true'),
(17, '2026-03-20', '15:50:13', 'B3F28D1A', 'false'),
(18, '2026-03-25', '14:39:34', '04104792681190', 'true'),
(19, '2026-03-25', '14:40:50', '044492B2141590', 'false'),
(21, '2026-03-25', '14:49:05', '044492B2141590', 'true'),
(22, '2026-03-25', '14:50:45', '0587BE8704B300', 'true'),
(23, '2026-03-25', '14:51:36', '04104792681190', 'false'),
(24, '2026-04-01', '13:24:10', 'BA2DC200', 'true'),
(25, '2026-04-01', '13:30:48', '04241E32A61290', 'true'),
(26, '2026-04-01', '13:32:58', '04241E32A61290', 'true'),
(27, '2026-04-01', '13:37:31', '04241E32A61290', 'false'),
(28, '2026-04-01', '13:41:50', '04241E32A61290', 'false'),
(30, '2026-04-01', '13:48:09', 'BA2DC200', 'false'),
(31, '2026-04-01', '13:49:52', 'BA2DC200', 'false'),
(34, '2026-04-01', '13:57:46', 'BA2DC200', 'false'),
(35, '2026-04-01', '14:09:18', '04241E32A61290', 'false'),
(43, '2026-04-01', '15:28:01', 'BA2DC200', 'false'),
(44, '2026-04-01', '15:28:01', 'BA2DC200', 'false'),
(45, '2026-04-01', '15:30:32', 'BA2DC200', 'false'),
(47, '2026-04-01', '15:40:54', 'CF946748', 'true'),
(48, '2026-04-01', '15:41:35', 'CF946748', 'true'),
(49, '2026-04-01', '15:41:52', 'CF946748', 'true'),
(50, '2026-04-01', '15:44:23', 'CF946748', 'true'),
(51, '2026-04-01', '15:45:35', 'CF946748', 'true');

-- --------------------------------------------------------

--
-- Structure de la table `tag`
--

CREATE TABLE `tag` (
  `id` varchar(100) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `pin` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `tag`
--

INSERT INTO `tag` (`id`, `nom`, `pin`) VALUES
('04104792681190', 'Bastien', 1111),
('04241E32A61290', 'Audrey_Baud', 123),
('044492B2141590', 'Nils', 6257),
('0819B225', 'Telefon', 0),
('B3F28D1A', 'Elsa_Sohn', 7491),
('BA2DC200', 'Baud', 2809),
('CF946748', 'Fanny_Santi', 5341);

-- --------------------------------------------------------

--
-- Structure de la table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `heure` varchar(11) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `uid` varchar(100) NOT NULL,
  `pin` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `test`
--

INSERT INTO `test` (`id`, `heure`, `nom`, `uid`, `pin`) VALUES
(21, '2025-12-12', 'CF946748', 'coucou', 0),
(47, '2026-3-20', 'Fanny_Santi', 'CF946748', 5341),
(48, '2026-3-20', 'Fanny_Santi', 'CF946748', 5341),
(49, '2026-3-20', 'nils', 'CF8949898516', 6767),
(50, '2026-3-20', 'nils', 'CF8949898516', 6767),
(51, '2026-3-20', 'nils', 'CF8949898516', 6767),
(52, '2026-3-20', 'Fanny_Santi', 'CF946748', 5341),
(53, '2026-3-20', 'Fanny_Santi', 'CF946748', 5341),
(54, '2026-3-20', 'Fanny_Santi', 'CF946748', 5341),
(55, '2026-3-20', 'Fanny_Santi', 'CF946748', 5341),
(56, '2026-3-20', 'Fanny_Santi', 'CF946748', 3333),
(57, '2026-3-20', 'nils', 'CF8949898516', 6767),
(58, '2026-3-20', 'Elsa_Sohn', 'B3F28D1A', 7491),
(59, '2026-3-20', 'Elsa_Sohn', 'B3F28D1A', 7491),
(60, '2026-3-20', '', '08403108', 0),
(61, '2026-3-20', '', '04104792681190', 0),
(62, '2026-3-20', '', '044DB232CE6180', 0),
(63, '2026-3-20', 'nils', 'CF8949898516', 6767),
(64, '2026-3-20', 'nils', 'CF8949898516', 6767),
(65, '2026-3-20', 'Elsa_Sohn', 'B3F28D1A', 7491),
(66, '2026-3-20', 'Elsa_Sohn', 'B3F28D1A', 3333),
(67, '2026-3-25', 'Bastien', '04104792681190', 1111),
(68, '2026-3-25', '', '044492B2141590', 0),
(69, '2026-3-25', 'Telefon', '0819B225', 0),
(70, '2026-3-25', 'Nils', '044492B2141590', 6257),
(71, '2026-3-25', 'Carta_magique', '0587BE8704B300', 2222),
(72, '2026-3-25', 'Bastien', '04104792681190', 8922),
(73, '2026-4-1', 'Baud', 'BA2DC200', 2809),
(74, '2026-4-1', 'Audrey_Baud', '04241E32A61290', 123),
(75, '2026-4-1', 'Audrey_Baud', '04241E32A61290', 123),
(76, '2026-4-1', 'Audrey_BAUD', '04241E32A61290', 2809),
(77, '2026-4-1', 'Audrey_BAUD', '04241E32A61290', 2809),
(78, '2026-4-1', 'Audrey', '04241E32A61290', 2809),
(79, '2026-4-1', 'e', 'BA2DC200', 123),
(80, '2026-4-1', 'e', 'BA2DC200', 123),
(81, '2026-4-1', 'e', 'BA2DC200', 123),
(82, '2026-4-1', 'e', 'BA2DC200', 123),
(83, '2026-4-1', 'e', 'BA2DC200', 123),
(84, '2026-4-1', 'Audrey', '04241E32A61290', 2809),
(85, '2026-4-1', 'Inconnu', 'BA2DC200', 0),
(86, '2026-4-1', '', 'BA2DC200', 0),
(87, '2026-4-1', 'in', 'BA2DC200', 0),
(88, '2026-4-1', 'Fanny_Santi', 'CF946748', 5341),
(89, '2026-4-1', 'Fanny_Santi', 'BA2DC200', 5341),
(90, '2026-4-1', 'Audrey', '04241E32A61290', 2809),
(91, '2026-4-1', 'Fanny_Santi', 'CF946748', 5341),
(92, '2026-4-1', 'Audrey_Baud', 'BA2DC200', 0),
(93, '2026-4-1', '', 'BA2DC200', 0),
(94, '2026-4-1', 'Audrey_Baud', 'BA2DC200', 0),
(95, '2026-4-1', '', 'BA2DC200', 0),
(96, '2026-4-1', 'Fanny_Santi', 'CF946748', 5341),
(97, '2026-4-1', 'Fanny_Santi', 'CF946748', 5341),
(98, '2026-4-1', 'Fanny_Santi', 'CF946748', 5341),
(99, '2026-4-1', 'Fanny_Santi', 'CF946748', 5341),
(100, '2026-4-1', 'Fanny_Santi', 'CF946748', 5341);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateurs`
--

CREATE TABLE `utilisateurs` (
  `id` varchar(15) NOT NULL,
  `mdp` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `utilisateurs`
--

INSERT INTO `utilisateurs` (`id`, `mdp`) VALUES
('admin', 'admin');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `detection`
--
ALTER TABLE `detection`
  ADD PRIMARY KEY (`num_detec`);

--
-- Index pour la table `tag`
--
ALTER TABLE `tag`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `utilisateurs`
--
ALTER TABLE `utilisateurs`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `detection`
--
ALTER TABLE `detection`
  MODIFY `num_detec` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT pour la table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
