matriz = []
qtd = 1

for i in range(4):
    linha = []
    for j in range(4):
        num = int(input(f"Digite o {qtd}º valor: "))
        qtd += 1
        linha.append(num)
    matriz.append(linha)

for linha in matriz:
    print(linha)
    
contagem = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            contagem += 1

print(f"Quantidade de valores maiores que 10 é igual a: {contagem}")