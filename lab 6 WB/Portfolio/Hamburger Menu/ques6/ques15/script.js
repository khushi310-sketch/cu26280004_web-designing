const counters = document.querySelectorAll(".counter");

let hasStarted = false;

function startCounters() {

    counters.forEach(function(counter) {

        const target = Number(counter.dataset.target);

        let count = 0;

        const increment = Math.ceil(target / 100);

        const updateCounter = function() {

            count += increment;

            if (count < target) {

                counter.textContent = count;

                setTimeout(updateCounter, 20);

            } else {

                counter.textContent = target;
            }
        };

        updateCounter();
    });
}

const statsSection = document.querySelector(".stats-section");

const observer = new IntersectionObserver(function(entries) {

    entries.forEach(function(entry) {

        if (entry.isIntersecting && !hasStarted) {

            hasStarted = true;

            startCounters();
        }
    });

}, {
    threshold: 0.4
});

observer.observe(statsSection);