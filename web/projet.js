document.addEventListener("DOMContentLoaded", function() {

    let badges = document.querySelectorAll("span");

    function verifierBadge(numero, statut) {
        if (statut === true) {
            badges[numero].textContent = "Validé";
            badges[numero].style.color = "green";
        } else {
            badges[numero].textContent = "Refusé";
            badges[numero].style.color = "red";
        }
    }
    // Badge 1 valide
    verifierBadge(0, true);

    // Badge 2 refusé
    verifierBadge(1, false);
}
);
