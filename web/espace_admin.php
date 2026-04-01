<?php
session_start();

// Vérifier si l'utilisateur est connecté
if (!isset($_SESSION['user_id'])) {
    header('Location: connexion.php');
    exit;
}

?>
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Projet RFID</title>
    <link rel="stylesheet" href="projet.css">
  </head>
  <body>

    <div id="pageflex">
    <a href="deconnexion.php">Se déconnecter</a>
    <h1>Espace admin</h1>
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
            <th>Détails</th>
            <th>Editer/supprimer</th>
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
          
          echo '<td>'.$row['date'].'</td>';
          
          echo '<td>'.$row['heure'].'</td>';

          echo '<td>'.$row['id_tag'].'</td>';
          
          echo '<td>'.$row['nom'].'</td>';

          echo '<td><a href="details.php?num_detec='.$row['num_detec'].'">Plus de détails</a></td>';

          echo '<td><a href="modifier.php?id='.$row['num_detec'].'"><img height=20 src="images/stylo.png"></a>';

          echo '<a href="supprimer_ligne.php?id='.$row['num_detec'].'"><img height=20 src="images/croix-rouge.png"></a></td>';

          echo '</tr>';
        }      
        ?>       
        </tbody>

    </table>
    </div>
    </body>
    <script src="projet.js"></script>
</html>
