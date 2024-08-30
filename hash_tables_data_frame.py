
from itertools import zip_longest
import pandas as pd

# Dicionário simples
dados = {
    "Nome": ["Alice", "Bob", "Charlie", "David"],
    "Idade": [25, 30, 35],  # Lista menor
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
}

print(dados)
print(dados.get("Nome"))
print(dados.get("Idade"))
print(dados.get("Cidade"))

print(dados.keys())
print(dados.values())

# Ajustando automaticamente o tamanho das listas
# Correção: zipa as listas e cria um dicionário para o DataFrame
dados_ajustados = list(zip_longest(*dados.values(), fillvalue=None))

# Convertendo para DataFrame
df = pd.DataFrame(dados_ajustados, columns=dados.keys())

# Exibindo o DataFrame
print(df)

input("Enter para sair...")
