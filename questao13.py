#13) Leia uma matriz 3 × 3 de inteiros e gere uma lista com a soma de cada coluna. Mostre a lista.

#Exemplo:

#  5  -8  10
#  1   2  15
#  25  10  7

matriz = [
    [5, -8, 10],
    [1, 2, 15 ],
    [25, 10, 7]
]

soma_linhas = []

for linha in matriz:
    total_linha = 0
    for elemento in linha:
        total_linha += elemento  # Soma dos elementos
    soma_linhas.append(total_linha)

print(soma_linhas)

