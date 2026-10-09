numeros = []

    # 1. Leitura dos 10 números
for i in range(10):
    num = int(input("Digite o  número: "))
    numeros.append(num)

    # 2.valor de X
    x= int(input("Digite o valor de x: "))

multiplos= []

    #  contagem dos múltiplos
for num in numeros:
        if num % x == 0:
            multiplos.append(num)

print("Quantidade de múltiplos de x", len(multiplos))
print("Múltiplos encontrados:", multiplos)
