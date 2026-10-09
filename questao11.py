matriz = []
qtd = 1

for i in range(4):
    linha = []
    for j in range(4):
        numero = int(input(f"Digite o {qtd}º número: "))
        linha.append(numero)
        qtd += 1
        linha.append(numero)
    matriz.append(linha)

for linha in matriz:
    print(linha)

maior = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha_maior = i
            coluna_maior = j

print(f"O maior número da matriz é {maior}, localizado na linha {linha_maior} e coluna {coluna_maior}.")