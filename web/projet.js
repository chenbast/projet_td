console.log('salut');
let badges = document.querySelectorAll(".etat");
    
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