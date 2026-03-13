document.addEventListener("DOMContentLoaded", function() {

    let badges = document.querySelectorAll(".etat");

    function verifierBadge(numero, statut) {
        if (statut === true) {
            badges[numero].textContent = "Validé";
            badges[numero].style.color = "green";
        } else {
            badges[numero].textContent = "Refusé";
            badges[numero].style.color = "red";
        }
    }
    verifierBadge(0, true);   // Badge 1 validé
    verifierBadge(1, false);  // Badge 2 refusé
}
);