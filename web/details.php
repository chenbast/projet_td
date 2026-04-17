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
    </nav>

    <div id="pageflex">
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
            <th>Date de détection</th></the>
            <th>Heure de détection</th>
            <th>ID Badge</th>
            <th>Propriétaire</th>
          </tr>
        </thead>
        <tbody>

        <?php
        
        if(isset($_GET['num_detec'])){
            $id=$_GET['num_detec'];
            $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');
            $sql="SELECT * FROM detection d JOIN tag t ON d.id_tag=t.id WHERE d.num_detec=$id";
            $result = $dbh->query($sql);
            while($row = $result->fetch(PDO::FETCH_ASSOC)){
                echo'<tr><td>'.$row['num_detec'].'</td>';
          
                echo'<td class="etat" autorisation="'.$row['autorisation'].'"></td>';
                
                echo '<td>'.$row['date'].'</td>';
                
                echo '<td>'.$row['heure'].'</td>';
      
                echo '<td>'.$row['id_tag'].'</td>';
                
                echo '<td>'.$row['nom'].'</td>';
      
                echo '</tr>';
            }
        }
        ?>
        </tbody>
            <img height=80 src="images/fleche_retour.png">
            <a href="index.php">Retour</a>

    </table>
    </div>
    </body>
    <script src="projet.js"></script>
</html>
