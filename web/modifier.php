<!doctype html>
<html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Modifier la ligne</title>
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
    <h1>Modifier la ligne</h1>
    
    <div class="flex_horizontal">
          <table id="tableBadges">
        <thead>
          <tr>
            <th>Numéro de détection</th>
            <th>État du badge</th>
            <th>Date de détection</th></the>
            <th>Heure de détection</th>
            <th>ID Badge</th>
            <th>Propriétaire</th>
            <th class="jaune">Editer/supprimer</th>
          </tr>
        </thead>

        <tbody>
        <?php
        $dbh = new PDO('mysql:dbname=projet_rfid;host=localhost;charset=utf8', 'root', '');
        $id=$_GET['id'];
        $sql="SELECT * FROM detection d JOIN tag t ON d.id_tag=t.id WHERE num_detec=$id";
        $result = $dbh->query($sql);
        while($row = $result->fetch(PDO::FETCH_ASSOC)){
            
          echo '<form method="post" action="valider.php?id='.$row['num_detec'].'" enctype="multipart/form-data">';

          echo'<tr><td>'.$row['num_detec'].'</td>';
          
          echo'<td> <span class="etat" autorisation="'.$row['autorisation'].'"></span><select id="autorisation"><option class="etat" autorisation="true"></option><option class="etat" autorisation="false"></option></select></td>';
            
          echo '<td><input type="date" name="date" id="date" value="'.$row['date'].'"></td>';
          
          echo '<td><input type="text" name="heure" id="heure" value="'.$row['heure'].'"></td>';

          echo '<td>'.$row['id_tag'].'</td>';
          
          echo '<td>'.$row['nom'].'</td>';

          echo '<td class="jaune">Editer</td>';

          echo '</tr>';
        }      
        ?>
    <img height=80 src="images/fleche_retour.png">
    <a href="espace_admin.php">Retour</a>
    </div>
    <input type="submit"></form>
    </body>
    
    <script src="projet.js"></script>
</html>
