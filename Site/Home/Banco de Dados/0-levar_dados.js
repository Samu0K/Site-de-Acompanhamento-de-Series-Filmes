const API_URL = "http://127.0.0.1:5000";

const levar = document.getElementById("botao_confirmar")
levar.addEventListener("click", async function (event) {

    event.preventDefault()
    const nome = document.getElementById("nome").value
    const apelido = document.getElementById("apelido").value
    const email = document.getElementById("email").value
    const idade = document.getElementById("data_nascimento").value
    const senha = document.getElementById("senha").value

    fetch("http://127.0.0.1:5000", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
    },
        body: JSON.stringify(
            {
                "nome": nome,
                "apelido": apelido,
                "email": email,
                "idade": idade,
                "senha": senha
            }
        )})
        .then(response => response.json())
        .then(() => alert("Cadastro realizado com sucesso!"))
        .catch(error => console.error("Erro ao cadastrar:", error))
        })
