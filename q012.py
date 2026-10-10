# Cria uma matriz vazia
matriz = []

# Lê os números de uma matriz 3x3
for i in range(3):
    linha = []

    for j in range(3):
        num = int(input(f"Digite o número da posição [{i}][{j}]: "))
        linha.append(num)

    matriz.append(linha)

# Mostra a matriz
print("\nMatriz:")
for linha in matriz:
    print(linha)

# Calcula a soma da diagonal principal
soma = 0