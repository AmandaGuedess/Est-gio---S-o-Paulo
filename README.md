# Desafio de Lógica com Python - Estágio

Este repositório contém soluções para vários desafios de lógica e programação utilizando a linguagem Python. Cada solução foi desenvolvida com o objetivo de praticar conceitos básicos e intermediários de lógica de programação, manipulação de dados e análise.

## Desafios resolvidos

### 1. Cálculo da variável SOMA
**Descrição:**
Dado o código abaixo, o desafio consiste em calcular o valor final da variável `SOMA` após o loop:
```python
int INDICE = 13, SOMA = 0, K = 0;
while (K < INDICE) {
    K = K + 1;
    SOMA = SOMA + K;
}
Imprimir(SOMA);
```

### 2. Sequência de Fibonacci
**Descrição:**
Escreva um programa que, dado um número, informe se ele pertence à sequência de Fibonacci.
```python
def pertence_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {n} não pertence à sequência de Fibonacci."

n = 21  # Número de exemplo
print(pertence_fibonacci(n))
```
### 3. Faturamento diário
**Descrição:**
Dado o faturamento diário de uma distribuidora, o programa deve calcular:

- O menor valor de faturamento ocorrido em um dia do mês.
- O maior valor de faturamento ocorrido em um dia do mês.
- O número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
```python
import json

# Carregar os dados do JSON
with open('dados.json', 'r') as f:
    faturamento = json.load(f)

# Remover dias sem faturamento
faturamento_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

# Calcular menor e maior valor de faturamento
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)

# Calcular a média mensal
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

# Contar dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
```
### 4. Percentual de faturamento por estado
**Descrição**
Dado o faturamento mensal de uma distribuidora detalhado por estado, calcule o percentual de representação de cada estado no valor total.
```python
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento_estados.values())

percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estados.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

```
### 5. Inversão de string
**Descrição:**
Escreva um programa que inverta os caracteres de uma string sem usar funções prontas.
```python
def inverter_string(s):
    invertida = ''
    for i in range(len(s)-1, -1, -1):
        invertida += s[i]
    return invertida

string = "exemplo"
print(inverter_string(string))
```

