<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Projet RFID stats</title>
        <link rel="stylesheet" href="projet.css">
    </head>
    <body>
    <img class="icons" id="menu" src="images/menu.png" alt="image_menu">
    <nav id="navigation">
      <img class="icons" id="croix" src="images/croix.png" alt="image_croix">
      <a href="index.php">Accueil</a>
      <a href="stats.php">Stats</a>
    </nav>

    <div id="pageflex">
    <h1> Statistiques</h1>
    <div id="mainflex">
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid1">
      <h1> Projet RFID</h1>
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid2">
    </div>
    
        <form method="post" action="date.php" enctype="multipart/form-data">
        <p>
            <label for="date1">Rechercher par date :</label>
            <br>
            <input type="date" name="date1" id="date1">
        </p>
        <p>
	        <input type="submit" value="Rechercher">
        </p>
        </form>
        
        <form method="post" action="nom.php" enctype="multipart/form-data">
        <p>
            <label for="nom">Rechercher par nom :</label>
            <br>
            <select name="nom" id="nom">
                <?php
                $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');

                $sql="SELECT nom FROM tag";
                $result = $dbh->query($sql);
                while($row = $result->fetch(PDO::FETCH_ASSOC)){
                    echo '<option value="'.$row['nom'].'">'.$row['nom'].'</option>';
                }
                ?>
            </select>

        </p>
        <p>
	        <input type="submit" value="Rechercher">
        </p>
  
        </form>
    </div>
    </body>
    <script src="projet.js"></script>
</html>
