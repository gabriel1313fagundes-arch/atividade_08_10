#14) Leia 10 números inteiros em uma lista e escreva quais elementos são **números primos**, acompanhados de suas posições na lista.

lista = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    lista.append(numero)