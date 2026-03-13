<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Projet RFID</title>
    <link rel="stylesheet" href="projet.css">
    <script src="projet.js"></script>
  </head>
  <body>
    <div id="mainflex">
      <img src="images\rfid.png" alt="sticker rfid1">
      <h1> Projet RFID</h1>
      <img src="images\rfid.png" alt="sticker rfid2">
    </div>
    <br>
    <table id="tableBadges">
        <thead>
          <tr>
            <th>Numéro de détection</th>
            <th>État du badge</th>
            <th>Date de détéction</th></the>
            <th>Heure de détection</th>
            <th>ID Badge</th>
            <th>propriétaire</th>
          </tr>
        </thead>

        <tbody>
        <?php
        $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');

        $sql="SELECT * FROM detection d JOIN tag t ON d.id_tag=t.id";
        $result = $dbh->query($sql);
        while($row = $result->fetch(PDO::FETCH_ASSOC)){
          echo'<tr><td>'.$row['num_detec'].'</td>';
          
          echo'<td class="etat"></td>';
          
          echo '<td>'.$row['date'].'</td>';
          
          echo '<td>'.$row['heure'].'</td>';

          echo '<td>'.$row['id_tag'].'</td>';
          
          echo '<td>'.$row['type_tag'].'</td></tr>';
        }      
        ?>       
        </tbody>

    </table>

    </body>
</html>
