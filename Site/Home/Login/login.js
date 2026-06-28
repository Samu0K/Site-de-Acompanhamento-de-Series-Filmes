document.addEventListener("DOMContentLoaded",() => {
    const formLogin = document.getElementById("form-login");
    formLogin.addEventListener("submit", login);
})

async function login(event) {
    event.preventDefault();

    const email = document.getElementById("login-email").value
    const senha = document.getElementById("login-senha").value


    const resposta = await fetch ("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, senha })
    })

    const dados = await resposta.json()

    if (resposta.ok) {
        localStorage.setItem("usuario", JSON.stringify(dados))
        window.location.href = "../Main/index.html"
    } else {
        const msg = document.getElementById("msg-login")
        msg.textContent = dados.erro
        msg.style.display = "block"
    }
}
