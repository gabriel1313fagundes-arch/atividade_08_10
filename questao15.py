lista = [9.0, 1.0, 5.0, 8.0, 2.0, 4.0, 7.0, 3.0, 6.0, 0.0]
#Lista com os números

# Algoritmo de ordenação (Bubble Sort)
n = len(lista)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            # Troca os elementos de posição
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Converte para inteiro antes de exibir para remover as casas decimais
lista_inteiros = [int(x) for x in lista]

# Exibição compacta sem colchetes nem pontos decimais
print("Lista ordenada:", *lista_inteiros)
