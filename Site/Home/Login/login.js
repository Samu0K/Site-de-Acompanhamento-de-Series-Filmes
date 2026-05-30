document.addEventListener("DOMContentLoaded",() => {
    const formLogin = document.getElementById("form-login");
    formLogin.addEventListener("submit", login);
})

async function login(event) {
    event.preventDefault();

    const email = document.getElementById("login-email").value
    const senha = document.getElementById("login-senha").value
    