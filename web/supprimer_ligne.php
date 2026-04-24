<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Supprimer la ligne</title>
        <link rel="stylesheet" href="projet.css">
    </head>
    <body>
    <img class="icons" id="menu" src="images/menu.png" alt="image_menu">
    <nav id="navigation">
      <img class="icons" id="croix" src="images/croix.png" alt="image_croix">
      <a href="index.php">Accueil</a>
      <a href="stats.php">Stats</a>
      <a href="connexion.php">Espace admin</a>
    </nav>
    
    <div class="flex_horizontal">
    <?php
    //on obtient l'id de la detection à supprimer grace au GET dans le lien php
        $numDetec = $_GET['id'];
        $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');
        $result = $dbh->query("DELETE FROM detection WHERE num_detec = $numDetec");
        echo '<p>';
        echo "La détection n°".$numDetec." a bien été supprimé</p>";
    ?>
    <img height=80 src="images/fleche_retour.png">
    <a href="espace_admin.php">Retour</a>
    </div>
    </body>
    
    <script src="projet.js"></script>
</html>
