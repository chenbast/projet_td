<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Projet RFID</title>
    <link rel="stylesheet" href="projet.css">
  </head>
  <body>
    <img class="icons" id="menu" src="images/menu.png" alt="image_menu">
    <nav id="navigation">
      <img class="icons" id="croix" src="images/croix.png" alt="image_croix">
      <a href="index.php">Accueil</a>
      <a href="stats.php">Rechercher</a>
      <a href="espace_admin.php">Espace admin</a>
    </nav>

    <div id="pageflex">
    <h1>Accueil</h1>
    <div id="mainflex">
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid1">
      <h1> Projet RFID</h1>
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid2">
    </div>

    <table id="tableBadges">
        <thead>
          <tr>
            <th>Numéro de détection</th>
            <th>État du badge</th>
            <th>Propriétaire</th>
            <th>Détails</th>
          </tr>
        </thead>

        <tbody>
        <?php
        $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');

        $sql="SELECT * FROM detection d JOIN tag t ON d.id_tag=t.id";
        $result = $dbh->query($sql);
        while($row = $result->fetch(PDO::FETCH_ASSOC)){
          echo'<tr><td>'.$row['num_detec'].'</td>';
          
          echo'<td class="etat" autorisation="'.$row['autorisation'].'"></td>';
          
          echo '<td>'.$row['nom'].'</td>';

          echo '<td><a href="details.php?num_detec='.$row['num_detec'].'">Plus de détails</a></td>';

          echo '</tr>';
        }      
        ?>       
        </tbody>

    </table>
    </div>
    </body>
    <script src="projet.js"></script>
</html>
