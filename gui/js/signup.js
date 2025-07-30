document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signup-form');
    const message = document.getElementById('signup-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value;
        const confirm = document.getElementById('confirm').value;

        if (password !== confirm) {
        message.textContent = "Passwords do not match.";
        message.style.color = "var(--error-color)";
        return;
        }

        // Call Python function
        console.log("I'm still here")
        const response = await eel.handle_signup(username, password)();

        // Show message from Python
        message.textContent = response.message;
        message.style.color = response.success ? "green" : "var(--error-color)";
    });
});
