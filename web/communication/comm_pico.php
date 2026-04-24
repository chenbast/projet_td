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
//cette page sert uniquement à la récupération de données lorsque on scan un badge
$dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');

if(isset($_GET['uid'])&&isset($_GET['nom'])&&isset($_GET['pin'])){
	$uid=$_GET['uid'];
	$nom=$_GET['nom'];
	$pin=$_GET['pin'];

	$date=date("Y-n-j");
	$heure=date("H:i:s");

	$sql="SELECT * FROM tag WHERE id='$uid'";
	$result=$dbh->query($sql);
	if ($result->rowCount() == 0){//si le tag n'existe pas encore dans la bd, on l'ajoute
		echo'nouveau tag detecte';
		$sql="INSERT INTO tag (id,nom,pin) VALUES ('$uid','$nom','$pin')";
		$dbh->query($sql);
	}
	//ensuite quoi qu'il arrive, on ajoute la détections aux autres détections
	$sql="SELECT pin FROM tag WHERE id='$uid'";
	$result=$dbh->query($sql);
	while($row=$result->fetch(PDO::FETCH_ASSOC)){
		$pin_valide=$row['pin'];
	}
	if($pin_valide==$pin){
		//si le code pin est le bon, on valide la détection
		$sql="INSERT INTO detection (date,heure,id_tag,autorisation) VALUES ('$date','$heure','$uid','true')";
	}
	else{
		//sinon, on indique qu'elle est invalide
		$sql="INSERT INTO detection (date,heure,id_tag,autorisation) VALUES ('$date','$heure','$uid','false')";
	}
	$result=$dbh->query($sql);

}
?>
</body>
</html>