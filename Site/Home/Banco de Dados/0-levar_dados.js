const API = "http://localhost:5000"

function mostrarMensagem(elementoId, texto, tipo = "erro") {
    const elemen = document.getElementById(elementoId);
    if (!elemen);
    elemen.textContent = texto;
    elemen.className = 'mensagem ${tipo}';
    elemen.style.display = 'block';
    setTimeout(() => {elemen.style.display = 'none';}, 4000);
}



async function cadastrar(event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value.trim();
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (!nome || !email || !senha) {
        mostrarMensagem("mensagem", "Preencha todos os campos!", "erro");
        return;
    }
    
}


try {
    const resposta = await fetch ('${API}/cadastro', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nome, email, senha})
    });

    const data = await resposta.json();

    if (resposta.ok) {
        mostrarMensagem("mensagem", data.mensagem, "sucesso");
        document.getElementById("inscriçao").reset();
    } else {
        mostrarMensagem("mensagem", data.erro, "erro");
    }
} catch(error) {
    mostrarMensagem("mensagem", "Erro ao cadastrar usuário.", "erro");
}


async function login(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    try {
        const resposta = await fetch('${API}/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({email, senha})
        });

        const data = await resposta.json();

        if (resposta.ok) {
            mostrarMensagem("mensagem", data.mensagem, "sucesso");
            document.getElementById("botao_confirmar").reset();
            atualizarUILogado(data.nome);
        } else {
            mostrarMensagem("mensagem", data.erro, "erro");
        }
    } catch {
        mostrarMensagem("mensagem", "Erro ao fazer login.", "erro");
    }
}


async function logout() {
    await fetch('${API}/logout', {
        method: 'POST', credentials: 'include'});
    atualizarUILogado();
}


function atualizarUILogado(nome) {
    const secaoAuth = document.getElementById("secao-auth");
    const secaoUsuario = document.getElementById("secao-usuario");
    const nomeUsuario = document.getElementById("nome-usuario");

    if (secaoAuth) secaoAuth.style.display = "none";
    if (secaoUsuario) secaoUsuario.style.display = "block";
    if (nomeUsuario) nomeUsuario.textContent = nome;
}

function atualizarUIDeslogado() {
    const secaoAuth = document.getElementById("secao-auth");
    const secaoUsuario = document.getElementById("secao-usuario");

    if (secaoAuth) secaoAuth.style.display = "block";
    if (secaoUsuario) secaoUsuario.style.display = "none";
}


async function carregarSeries() {
    const Lista