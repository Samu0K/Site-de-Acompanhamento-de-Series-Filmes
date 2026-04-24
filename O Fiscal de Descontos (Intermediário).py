cliente = []
while True:
        cliente.append(input("Digite o nome do cliente: "))
        if (input("deseja incluir outro cliente? (s/n): ") == "n"):
            print(f"Clientes registrados: {cliente}, quantidade de clientes: {len(cliente)}, o primeiro cliente registrado é: {cliente[0]}, o ultimo cliente registrado é: {cliente[-1]}")
            break






informatica = float(input("digite o valor gasto em informática: ")) 
acessorios = float(input("digite o valor gasto em acessórios: "))

if (informatica >= 500 ):
    print(f"Sua compra em informatica é de {informatica - (informatica * 0.10)}, parabens, você ganhou um desconto de 10%")
else: 
    print("Infelizmente, você não ganhou um desconto de 10% em informática,")

print(f"seu desconto em acessórios é de 15%, o valor total da sua compra é de: {acessorios - (acessorios * 0.15)}")





estoque = {"tenis": 100, "camisa": 50, "calça": 120, "boné": 20}
maior_estoque = {}
menor_estoque = {}

for produto, estoque in estoque.items():
    if (estoque >= 100):
        maior_estoque[produto] = estoque
    else: 
        menor_estoque[produto] = estoque
        
print(f"Os produtos com o valor maior ou igual a 100 são: {maior_estoque}")
print(f"Os produtos com o valor menor que 100 são: {menor_estoque}")


usuarios = {"samuel": "1234", "ana": "1234"}

while True:
    input_usuario = input("Digite seu nome de usuário: ")
    input_senha = input("Digite sua senha: ")
    if input_usuario in usuarios and usuarios[input_usuario] == input_senha:
        print("Login realizado com sucesso!")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.")