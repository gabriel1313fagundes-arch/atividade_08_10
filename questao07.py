numeros = []
quantidade = 0

# 1. Leitura dos 10 números inteiros para a lista
for i in range(5):
    num = int(input("Digite o número: "))
    numeros.append(num)

pares = []

# 2. Contagem e separação dos números pares (num % 2 == 0)
for numero in numeros:
    if numero % 2 == 0:
        quantidade += 1
        pares.append(numero)

# 3. Exibição do resultado
print(f"Lista digitada:", numeros)
print(f"Quantidade de números pares:",  quantidade)
print(f"Números pares encontrados:", pares)
