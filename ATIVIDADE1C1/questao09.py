# Cria uma matriz vazia
matriz = []

# Inicia o contador de números maiores que 10
contador = 0

# Percorre as 4 linhas da matriz
for i in range(4):
    linha = []

    # Percorre as 4 colunas da matriz
    for j in range(4):

        # Pede ao usuário um número inteiro
        numero = int(input(f"Digite o número [{i}][{j}]: "))

        # Adiciona o número na linha
        linha.append(numero)

        # Verifica se o número é maior que 10
        if numero > 10:
            contador += 1

    # Adiciona a linha completa na matriz
    matriz.append(linha)

# Mostra a matriz completa na tela
print("\nMatriz 4x4:")
for linha in matriz:
    print(linha)

# Mostra a quantidade de números maiores que 10
print("\nQuantidade de números maiores que 10:", contador)