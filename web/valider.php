<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Projet RFID</title>
    <link rel="stylesheet" href="projet.css">
  </head>
  <body>
    <div class="flex_horizontal">
      <br><br><br>
        <?php
        //récupération des données du formulaire envoyé
        $new_date=$_POST['date'];
        $new_heure=$_POST['heure'];
        $numDetec = $_GET['id'];
        $new_autorisation = $_POST['autorisation'];
        $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');
        //requete SQL pour modifier des données spécifiques
        $sql = "UPDATE detection SET `date` = '$new_date', heure = '$new_heure', autorisation = '$new_autorisation' WHERE num_detec = $numDetec";
        $result = $dbh->query($sql);
        echo 'La détection n°'.$numDetec.' a bien été changé avec la date '.$new_date.', avec la date '.$new_heure.' et une autorisation '.$new_autorisation.'.';    
        
        ?> 
      <img height=80 src="images/fleche_retour.png">
      <a href="espace_admin.php">Retour</a>      
    </div>
    </body>
    <script src="projet.js"></script>
</html>
