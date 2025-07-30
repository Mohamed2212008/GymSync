document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('login-form');
    const login_message = document.getElementById('login_message');

    document.addEventListener('submit', async (e) => {
        e.preventDefault();

        // fetch data from the form
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value;

        // call the python function
        const response = await eel.handle_login(username, password)();

        // Show message from Python
        login_message.textContent = response.message;
        login_message.style.color = response.success ? "green" : "var(--error-color)";
    });
});