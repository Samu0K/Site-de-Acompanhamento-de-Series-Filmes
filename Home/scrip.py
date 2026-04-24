import json
import os
import csv

# 1. Nossa "Base de Dados" (Simulando o que viria do JSON)
vendas_json = [
    {"produto": "Teclado Gamer", "valor": 150, "setor": "Informatica"},
    {"produto": "Mouse Pad", "valor": 30, "setor": "Informatica"},
    {"produto": "Monitor 24p", "valor": 850, "setor": "Monitores"},
    {"produto": "Cabo HDMI", "valor": 45, "setor": "Acessorios"}
]

# 2. Criando a lista vazia para o que vamos filtrar
vendas_filtradas = []
total_vendas = 0
# --- SUA VEZ: PARTE 1 (Lógica de Filtro) ---
# Use um 'for' para percorrer 'vendas_json'
# Use um 'if' para verificar se o 'valor' é maior que 100
# Se for verdade, use o '.append()' para colocar na lista 'vendas_filtradas'

for venda in vendas_json:
    # ESC # Remova o pass e complete
    if (venda["valor"] > 100): vendas_filtradas.append(venda)
    else: pass 
    if venda["valor"] > 100:
        vendas_filtradas.append(venda)

# --- SUA VEZ: PARTE 2 (Exportação para CSV) ---
# Agora vamos salvar a lista 'vendas_filtradas' em um arquivo chamado 'vendas_altas.csv'

colunas = ["produto", "valor", "setor"]

with open("vendas_altas.csv", "w", newline="", encoding="utf-8") as f:
    # 1. Crie o escritor (DictWriter)
    # 2. Escreva o cabeçalho (writeheader)
    # 3. Escreva as linhas (writerows)
    
    vendas_altas = csv.DictWriter(f, fieldnames=colunas)
    vendas_altas.writeheader()
    vendas_altas.writerows(vendas_filtradas)

total_vendas = sum(venda["valor"] for venda in vendas_filtradas)
print(f"o total de vendas acima de 100 é: {total_vendas}")



# 1. Crie uma lista vazia para guardar os dados que vamos ler
dados_lidos = []

# 2. Abra o arquivo 'vendas_altas.csv' em modo de leitura ('r')
with open("clientes_registrados.csv", "r", encoding="utf-8") as f:
with open("vendas_altas.csv", "r", encoding="utf-8") as f:
    
    # 3. Crie o leitor usando csv.DictReader(f)
    leitor = csv.DictReader(f)
    
    # 4. Use um loop 'for' para percorrer o 'leitor'
    for linha in leitor:
        # Cada 'linha' já é um dicionário! 
        # Tente adicionar essa 'linha' na sua lista 'dados_lidos'
        if linha: dados_lidos.append(linha)
        

# 5. Fora do 'with', imprima a lista para ver se deu certo
print(dados_lidos)

print([1,0,0])