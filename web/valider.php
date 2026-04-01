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
        echo $new_date;
        echo $new_heure;
        echo $numDetec;
        $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');

        $result = $dbh->query("UPDATE detection SET date = $new_date, heure = $new_heure WHERE num_detec = $numDetec");

          echo 'La détection n°'.$numDetec.' a bien été changé avec la date '.$new_date.' et avec la date '.$new_heure.'.';    
        ?>       

    </div>
    </body>
    <script src="projet.js"></script>
</html>
