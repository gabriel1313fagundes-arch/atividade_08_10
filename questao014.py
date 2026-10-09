# Cria uma lista vazia
numeros = []

# Lê 10 números inteiros digitados pelo usuário
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

# Mostra a lista completa
print("\nLista:", numeros)

# Verifica quais números são primos
print("\nNúmeros primos e suas posições:")

for i in range(10):
    num = numeros[i]
    primo = True

    # Números menores que 2 não são primos
    if num < 2:
        primo = False
    else:
        # Testa se o número é divisível por algum número
        # entre 2 e ele mesmo, sem contar o próprio número
        for j in range(2, num):
            if num % j == 0:
                primo = False
                break

    # Se for primo, mostra o número e sua posição
    if primo:
        print(f"{num} (posição {i})")