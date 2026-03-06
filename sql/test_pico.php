<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>Titre de la page</title>
  <link rel="stylesheet" href="style.css">
  <script src="script.js"></script>
</head>
<body>
Coucou : <br>
<?php

$dbh = new PDO('mysql:dbname=projet_rfid ;host=localhost ;charset=utf8', 'root', '');

if ($_SERVER["REQUEST_METHOD"] == "GET") {
	if(isset($_GET['nombre'])){
		$test = $_GET['nombre'];
		echo $test;

	}
}
?>
</body>
</html>