const form = document.getElementById("contactForm");

form.addEventListener("submit", function(event) {

    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    const errorMessage = document.getElementById("errorMessage");

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (name === "") {
        errorMessage.textContent = "Please enter your name.";
        return;
    }

    if (!emailPattern.test(email)) {
        errorMessage.textContent = "Please enter a valid email address.";
        return;
    }

    if (message === "") {
        errorMessage.textContent = "Please enter your message.";
        return;
    }

    errorMessage.style.color = "green";
    errorMessage.textContent = "Form submitted successfully!";

    form.reset();
});