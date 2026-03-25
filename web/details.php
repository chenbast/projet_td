<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Projet RFID</title>
    <link rel="stylesheet" href="projet.css">
  </head>
  <body>
    <div id="mainflex">
      <img src="images\rfid.png" alt="sticker rfid1">
      <h1> Projet RFID</h1>
      <img src="images\rfid.png" alt="sticker rfid2">
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

    </table>

    </body>
    <script src="projet.js"></script>
</html>
