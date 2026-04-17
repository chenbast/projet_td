<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Visualisation Date</title>
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
      
    <?php
      echo '<h1>'.$_POST['date1'].'</h1>';
    ?>
    
    <div id="mainflex">
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid1">
      <h1> Projet RFID</h1>
      <img class="img_rfid" src="images\rfid.png" alt="sticker rfid2">
    </div>
        <table id="tableBadges">
        <thead>
          <tr>
            <th>État du badge</th>
            <th>Date de détection</th></the>
            <th>Heure de détection</th>
            <th>ID Badge</th>
            <th>Propriétaire</th>
          </tr>
        </thead>
    <?php
            $date1=$_POST['date1'];
            $dbh=new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');
            $sql='SELECT * FROM detection d JOIN tag t ON t.id = d.id_tag WHERE date = ';
            $sql = $sql."'".$date1."'";
            $result = $dbh->query($sql);
            echo "<p>Détections lors de la date ".$date1." : </p><br><br>";
            while($row = $result->fetch(PDO::FETCH_ASSOC)){
          
                echo'<tr><td class="etat" autorisation="'.$row['autorisation'].'"></td>';
                
                echo '<td>'.$row['date'].'</td>';
                
                echo '<td>'.$row['heure'].'</td>';

                echo '<td>'.$row['id_tag'].'</td>';
                
                echo '<td>'.$row['nom'].'</td>';

                echo '</tr>';

            }
            echo'</table>';
        ?>
        <img height=80 src="images/fleche_retour.png">
        <a href="stats.php">Retour</a> 
    </body>
    </div>
    <script src="projet.js"></script>
</html>