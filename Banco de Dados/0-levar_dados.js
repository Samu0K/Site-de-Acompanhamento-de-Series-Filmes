const levar = document.getElementById("tela_de_cadastro.html")
levar.addEventListener("submit", function(event){
    event.preventDefault()
    const nome = document.getElementById("nome").value
    const apelido = document.getElementById("apelido").value
    const email = document.getElementById("email").value
    const idade = document.getElementById("idade").value
    const senha = document.getElementById("senha").value
})

fetch("http://127.0.0.1:3000/Home/Cadastro/tela_de_cadastro.html?vscode-livepreview=true", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify()})
    .then(response => response.json())
    .then(alerta("Cadastro realizado com sucesso!"))
    .catch(error => console.error("Erro ao cadastrar:", error))
