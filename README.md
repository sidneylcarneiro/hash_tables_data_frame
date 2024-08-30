
```markdown
# Dicionário para DataFrame com Pandas

Este projeto demonstra como ajustar listas de tamanhos diferentes em um dicionário e convertê-las em um DataFrame utilizando a biblioteca `pandas` no Python.

## Descrição

O código apresenta um dicionário com três chaves: "Nome", "Idade" e "Cidade". As listas associadas a essas chaves possuem tamanhos diferentes. Para criar um DataFrame utilizando essas listas, é necessário ajustá-las para que todas tenham o mesmo comprimento. Isso é feito utilizando o método `zip_longest` da biblioteca `itertools`, que preenche as listas menores com valores `None`.

Após o ajuste, o dicionário é convertido em um DataFrame utilizando a biblioteca `pandas`.

## Exemplo de Código

```python
from itertools import zip_longest
import pandas as pd

# Dicionário simples
dados = {
    "Nome": ["Alice", "Bob", "Charlie", "David"],
    "Idade": [25, 30, 35],  # Lista menor
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
}

# Ajustando automaticamente o tamanho das listas
dados_ajustados = list(zip_longest(*dados.values(), fillvalue=None))

# Convertendo para DataFrame
df = pd.DataFrame(dados_ajustados, columns=dados.keys())

# Exibindo o DataFrame
print(df)
```

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale a biblioteca `pandas` caso ainda não tenha:
   ```bash
   pip install pandas
   ```
3. Execute o código Python.

## Saída Esperada

O código irá gerar um DataFrame onde as listas menores foram preenchidas com `None`:

```
      Nome  Idade           Cidade
0    Alice   25.0       São Paulo
1      Bob   30.0    Rio de Janeiro
2  Charlie   35.0  Belo Horizonte
3    David    NaN         Curitiba
```

## Licença

Este projeto é livre para uso pessoal e educacional.
```
