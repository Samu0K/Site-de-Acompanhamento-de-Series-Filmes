const botao = document.querySelector('.expan')

function aparecer(){
    const nome = ["Conta","Login","Cadastre-se"];
    nome.array.forEach(nome => {
        const novobotao = document.createElement('button');
        novobotao.innerText = nome;
        novobotao.classList.add("bnt-estilo");

        container.appendChild(novobotao)
        
    });
}

function carregarUsuario(){
    const dados = localStorage.getItem("usuario");
    if (dados) {
        const usuario = JSON.parse(dados);
        document.getElementById("nome-usuario").textContent = usuario.nome;
    } else {
        window.location.href = "../login/login.html";
    }
}
