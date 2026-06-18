const API = "http://localhost:5000"

function mostrarMensagem(elementoId, texto, tipo = "erro") {
    const elemen = document.getElementById(elementoId);
    if (!elemen) return;
    elemen.textContent = texto;
    elemen.className = `mensagem ${tipo}`;
    elemen.style.display = 'block';
    setTimeout(() => {elemen.style.display = 'none';}, 4000);
}



async function cadastrar(event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value.trim();
    const apelido = document.getElementById("apelido")?.value.trim() || "";
    const data_nascimento = document.getElementById("data_nascimento")?.value.trim() || "";
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (!nome || !email || !senha) {
        mostrarMensagem("mensagem", "Preencha todos os campos!", "erro");
        return;
    }
    
    try {
        const resposta = await fetch (`${API}/cadastro`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({nome, apelido, email, data_nascimento, senha})
    });

    const data = await resposta.json();

    if (resposta.ok) {
        mostrarMensagem("mensagem", data.mensagem, "sucesso");
        // O ID correto deve ser o do formulário (form-cadastro)
        const form = document.getElementById("form-cadastro") || document.getElementById("inscriçao");
        if (form) form.reset();
    } else {
        mostrarMensagem("mensagem", data.mensagem || data.erro, "erro");
    }
    } catch(error) {
        mostrarMensagem("mensagem", "Erro ao cadastrar usuário.", "erro");
    }
}


async function login(event) {
    event.preventDefault();

    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    try {
        const resposta = await fetch(`${API}/login`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({email, senha})
        });

        const data = await resposta.json();

        if (resposta.ok) {
            mostrarMensagem("mensagem", data.mensagem, "sucesso");
            // Botão não tem método reset(). Deve ser o formulário.
            const form = document.getElementById("form-login");
            if (form) form.reset();
            atualizarUILogado(data.nome);
        } else {
            mostrarMensagem("mensagem", data.erro, "erro");
        }
    } catch {
        mostrarMensagem("mensagem", "Erro ao fazer login.", "erro");
    }
}


async function logout() {
    await fetch(`${API}/logout`, {
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
    const lista = document.getElementById("lista-series");
    if (!lista) return;

    try {
        const resposta = await fetch(`${API}/series`, {credentials: 'include'});
        const series = await resposta.json();

        if (series.length === 0) {
            lista.innerHTML = "<p>Nenhuma série encontrada.</p>";
            return;
        }

        series.forEach((s) => {
        const card = document.createElement("div");
        card.className = "card-serie";
        card.innerHTML = `
            <h3>${s.titulo}</h3>
            <p><strong>Gênero:</strong> ${s.genero}</p>
            <p><strong>Ano:</strong> ${s.ano}</p>
            <p><strong>Temporadas:</strong> ${s.temporadas} &nbsp;|&nbsp;<strong>Episódios:</strong> ${s.episodios}</p>
        `;
        lista.appendChild(card);
    });
    } catch {
        if (lista) lista.innerHTML = "<p>Erro ao carregar séries.</p>";
    }
}


function mostrarCadastro() {
    document.getElementById("secao-login").style.display = "none";
    document.getElementById("secao-cadastro").style.display = "block";
}

function mostrarLogin() {
    document.getElementById("secao-cadastro").style.display = "none";
    document.getElementById("secao-login").style.display = "block";
}

document.addEventListener("DOMContentLoaded",() => {
    const formCadastro = document.getElementById("form-cadastro");
    const formLogin = document.getElementById("form-login");

    if (formCadastro) formCadastro.addEventListener("submit", cadastrar);
    if (formLogin) formLogin.addEventListener("submit", login);

    carregarSeries();
});
