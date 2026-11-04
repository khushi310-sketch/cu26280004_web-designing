const searchInput = document.getElementById("searchInput");

const projectCards =
    document.querySelectorAll(".project-card");


searchInput.addEventListener("input", function() {

    const searchValue =
        searchInput.value.toLowerCase();


    projectCards.forEach(function(card) {

        const projectText =
            card.textContent.toLowerCase();


        if (projectText.includes(searchValue)) {

            card.style.display = "block";

        } else {

            card.style.display = "none";
        }
    });
});