<?php
$dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');
$message = '';

if (isset($_POST['identifiant']) && isset($_POST['mdp'])) {
    $username = $_POST['identifiant'];
    $password = $_POST['mdp'];
    $sql = "SELECT * FROM utilisateurs WHERE id = '$username'";
    $result = $dbh->query($sql);
    while($row = $result->fetch(PDO::FETCH_ASSOC)){
        if($username==$row['id'] && $password==$row['mdp']){
            session_start();
            $_SESSION['user_id'] = $row['id'];
            header('Location: espace_admin.php');
        } else{
            $message = 'Mauvais identifiant ou mot de passe';
        }
    }
}
?>

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Connexion</title>
    <link rel="stylesheet" href="projet.css">
  </head>
  <body>
    <img class="icons" id="menu" src="images/menu.png" alt="image_menu">
    <nav id="navigation">
      <img class="icons" id="croix" src="images/croix.png" alt="image_croix">
      <a href="index.php">Accueil</a>
      <a href="stats.php">Rechercher</a>
      <a href="connexion.php">Espace admin</a>
    </nav>

    <div id="pageflex">
    <h1>Connexion</h1>

    <?php if (!empty($message)): ?>
        <p style="color:red"><?= $message ?></p>
    <?php endif; ?>

    <div id="mainflex">
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid1">
      <h1> Projet RFID</h1>
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid2">
    </div>

    <form class="flex_horizontal" method="post" action="connexion.php" enctype="multipart/form-data">
    <label for="identifiant">Identifiant :</label>
    <input class="connex" type="text" name="identifiant" id="identifiant">
    <label for="mdp">Mot de passe : </label>
    <input class="connex" type="password" name="mdp" id="mdp">
    <br>
    <input class="connex" type="submit" value="Connexion">
    </form>


    </div>
    </body>
    <script src="projet.js"></script>
</html>
