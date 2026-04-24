console.log('salut');//test du javascript
let badges = document.querySelectorAll(".etat");// récupération des données avec la class "etat"
    
function verifierBadge(numero) {
    //création d'une fonction pour afficher l'état des badges selon leur valeur de autorisation dans la base de donnée:

    let autorisation = badges[numero].getAttribute("autorisation");//récupération de l'état du badge avec l'attribut autorisation dans le php (qui est égal à $autorisation)
    if (autorisation == "true") {//si le badge est validé
        badges[numero].textContent = "Validé";
        badges[numero].style.color = "green";
    } else {//si le badge est refusé
        badges[numero].textContent = "Refusé";
        badges[numero].style.color = "red";
    }
}

for (let i = 0;i< badges.length; i++)  
    verifierBadge(i);//appliquer la fonction pour vérifer les badges à tout les badges

let menu = document.getElementById("menu");
menu.addEventListener("click",afficherMenu);

let croix = document.getElementById("croix");
croix.addEventListener("click",cacherMenu);
//on récupère les deux éléments cliquables grâce à leur ID et on leur ajoute un évènement lorsque
//on clique dessus

let nav = document.getElementById("navigation");

function cacherMenu(){
    //cacher le menu en réduisant la largeur de l'élément nav
    console.log("cache_menu");
    nav.style.width="0px";
}

function afficherMenu(){
    //on l'affiche en augmentant la largeur du nav
    console.log("affiche_menu");
    nav.style.width="100px";
}