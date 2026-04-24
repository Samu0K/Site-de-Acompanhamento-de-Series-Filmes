// Pegamos o valor digitado no campo de input
let nome = document.getElementById("nome").value;
let idade = parseInt(document.getElementById("idade").value); 

// Validação correta: verifica se a idade é menor que 10 (exemplo) ou não é um número
if (isNaN(idade) || idade < 10) {
    alert("Utilize uma idade válida (mínimo 10 anos)");
} else {
    console.log("Cadastro permitido para: " + nome);
}
