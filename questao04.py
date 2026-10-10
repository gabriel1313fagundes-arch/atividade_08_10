lista = []

for i in range(10): #Vai repetir a pergunta ao usuário por 10 vezes.
    num = int(input("Digite um número: "))
    lista.append(num) #Vai listar todos os números digitados em uma matriz.

maior = lista[0] #Vai guardar o maior número na variável maior.
posicao = 0 

for i in range(10):
    if lista[i] > maior: #Se o número da posição i for maior que o maior número, então:
        maior = lista[i] #Vai guardar o maior número na variável maior.
        posicao = i #Vai guardar a posição do maior número na variável posição.

print("\nA lista de números é:")
print(lista)
print("O maior número da lista é:", maior)
print("A posição do maior número é:", posicao)