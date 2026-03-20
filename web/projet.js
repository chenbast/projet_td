document.addEventListener("DOMContentLoaded", function() {
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

}
);