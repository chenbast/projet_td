-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 25 mars 2026 à 13:37
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
(1, '2026-03-01', '11:29:40', 'CF946748', 'true'),
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
(17, '2026-03-20', '15:50:13', 'B3F28D1A', 'false');

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
('04104792681190', '', 0),
('044DB232CE6180', '', 0),
('08403108', '', 0),
('B3F28D1A', 'Elsa_Sohn', 7491),
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
(66, '2026-3-20', 'Elsa_Sohn', 'B3F28D1A', 3333);

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
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `detection`
--
ALTER TABLE `detection`
  MODIFY `num_detec` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT pour la table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
