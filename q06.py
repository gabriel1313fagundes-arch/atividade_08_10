lista = []

for i in range(10):
    numero = int(input('Digite um número inteiro: '))
    lista.append(numero)

print('Lista antes:', lista)

for i in range(10):
    if lista[i] < 0:
        lista[i] = 0

print('Lista depois:', lista)
