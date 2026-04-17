<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Projet RFID</title>
    <link rel="stylesheet" href="projet.css">
  </head>
  <body>
        <?php
        $new_date=$_POST['date'];
        $new_heure=$_POST['heure'];
        $numDetec = $_GET['id'];
        $new_autorisation = $_GET['autorisation'];
        $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');
        $sql = "UPDATE detection SET `date` = '$new_date', heure = '$new_heure', autorisatio = $new_autorisation WHERE num_detec = $numDetec";
        $result = $dbh->query($sql);
        echo 'La détection n°'.$numDetec.' a bien été changé avec la date '.$new_date.' et avec la date '.$new_heure.'.';    
        
        ?> 
      <img height=80 src="images/fleche_retour.png">
      <a href="espace_admin.php">Retour</a>      
    </div>
    </body>
    <script src="projet.js"></script>
</html>
