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