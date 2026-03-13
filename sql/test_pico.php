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

$sql="SELECT * FROM detection d JOIN tag t ON d.id_tag=t.id";
$result = $dbh->query($sql);
while($row = $result->fetch(PDO::FETCH_ASSOC)){
	echo'<p>';
	echo'Numéro de détection : ';
	echo $row['num_detec'].'<br>';
	echo'Date et heure de passage : ';
	echo $row['date'].' à ';
	echo $row['heure'].'<br>';
	echo'Id et type du tag détecté : ';
	echo $row['id_tag'].' - '.$row['type_tag'];
	echo'</p>';
}

if(isset($_GET['test'])){
	$texte=$_GET['test'];
	echo $texte.'<br>';
	if(isset($_GET['autorisation'])){
		$auto=$_GET['autorisation'];
		echo $auto.'<br>';
		$sql="INSERT INTO test (heure,nom,autorisation) VALUES ('2025-12-12','$texte','$auto')";
		$dbh->query($sql);
	}
	else{
	$texte=$_GET['test'];
	echo $texte.'<br>';
	$sql="INSERT INTO test (heure,nom) VALUES ('2025-12-12','$texte')";
	$dbh->query($sql);
	}
}


echo "Affichage de la table test : <br>";
$sql="SELECT * FROM test";
$result = $dbh->query($sql);
while($row = $result->fetch(PDO::FETCH_ASSOC)){
	echo'<p>';
	echo'ID : ';
	echo $row['id'].'<br>';
	echo'Date : ';
	echo $row['heure'].'<br>';
	echo'Texte : ';
	echo $row['nom'].'<br>';
	echo'Autorisation : ';
	echo $row['autorisation'].'<br>';
	echo'</p>';
}


?>
</body>
</html>