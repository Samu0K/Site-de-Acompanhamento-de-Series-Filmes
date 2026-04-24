

while True:
    cpf = input("Digite o cpf do cliente: ")
    if len(cpf) != 11:
        print("-----------------------------------------")
        print("CPF inválido. O CPF deve conter exatamente 11 dígitos.")
    else:
        print("CPF válido!")
        break
    
nome = input("Digite o nome do cliente: ")
idade = input("Digite a idade do cliente: ")
print(f"Cliente registrado: {nome}, {idade} anos, CPF: {cpf}")
