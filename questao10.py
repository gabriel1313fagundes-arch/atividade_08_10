matriz = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
#Vai ler a qual é a linha e coluna, quando forem iguais, por exemplo; Linha 1 e Coluna 1; o resultado será igual 1, se forem diferentes, por exemplo; Linha 2 e Coluna 4; o resultado será 0
for linha in matriz:
    print(*(linha))
#Mostra o resultado da condicação imposta na linha 1   