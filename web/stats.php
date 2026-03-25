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
            <label for="date1">Entrez une date pour voir qui a badgé un badge sur le lecteur de badge à cette date</label>
            <br>
            <input type="date" name="date1" id="date1">
        </p>
        <p>
	        <input type="submit" value="rechercher une date">
        </p>
  
    </form>
</div>
    </body>
    <script src="projet.js"></script>
</html>
