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

$dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');

$sql="SELECT * FROM detection";
$result = $dbh->query($sql);
while($row = $result->fetch(PDO::FETCH_ASSOC)){
	echo'<p>';
	echo'Numéro de détection : ';
	echo $row['num_detec'].'<br>';
	echo'Date et heure de passage : ';
	echo $row['date'].' à ';
	echo $row['heure'].'<br>';
	echo'Type de tag détecté : ';
	echo'</p>';
}

// if ($_SERVER["REQUEST_METHOD"] == "GET") {
// 	if(isset($_GET['nombre'])){
// 		$test = $_GET['nombre'];
// 		echo $test;

// 	}
// }
?>
</body>
</html>