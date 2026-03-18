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
