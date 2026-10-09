################  ATIVIDADE 5 ###############

numeros = []
quantidade_negativo = 0
soma_positivo = 0

for i in range (10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

for numero in numeros:
    if numero < 0:
        quantidade_negativo += 1
    elif numero > 0:
        soma_positivo += numero

print("Os números digitados foram: ", numeros)
print("A quantidade de números negativos é: ", quantidade_negativo)
print("A soma dos números positivos é: ", soma_positivo)

############## ATIVIDADE 11 #############

matriz = [
    [4, 43, 10, 5],
    [11, 98, 23,7],
    [12, 45, 62, 9],
    [24, 56, 78, 100]
    ]

0 i e a linha
0 j e a coluna
    for i in range(len(matriz)):
    for j in range(len(matriz[i])):
    print("Linha:", i)
    print("Coluna:", j)
    print("Valor:", matriz[i][j])