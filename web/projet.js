console.log('salut');
let badges = document.querySelectorAll(".etat");
let badges_modif = document.querySelectorAll(".etat_modif"); 
    
function verifierBadge(numero) {
    let autorisation = badges[numero].getAttribute("autorisation");
    if (autorisation == "true") {
        badges[numero].textContent = "Validé";
        badges[numero].style.color = "green";
    } else {
        badges[numero].textContent = "Refusé";
        badges[numero].style.color = "red";
    }
}

function modifierBadges(numero){
    let valeur = badges_modif[numero].value; 
    if (valeur == "true") {
        badges_modif[numero].textContent = "Validé";
        badges_modif[numero].style.color = "green";
    } else {
        badges_modif[numero].textContent = "Refusé";
        badges_modif[numero].style.color = "red";
    }
}
for (let i = 0;i< badges.length; i++)  
    verifierBadge(i);

let menu = document.getElementById("menu");
menu.addEventListener("click",afficherMenu);

let croix = document.getElementById("croix");
croix.addEventListener("click",cacherMenu);

let nav = document.getElementById("navigation");

function cacherMenu(){
    console.log("cache_menu");
    nav.style.width="0px";
}

function afficherMenu(){
    console.log("affiche_menu");
    nav.style.width="100px";
}