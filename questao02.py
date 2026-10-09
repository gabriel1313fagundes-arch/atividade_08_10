lista = []
qtd = 1

for i in range(6):
#Vai repetir a pergunta ao usuário por 6 vezes.
    num = float(input(f"Digite o {qtd}° número: "))
    lista.append(num)
    #Vai listar todos os números digitados em uma matriz.
    qtd +=1

print("\nA lista na ordem inversa fica da seguinte forma: ")
i = len(lista) - 1
#Vai contar quantos números tem na lista e encontrar o último número.
while i >= 0:
    print(lista[i])
    i = i - 1
    #vai para a posição do próximo número a ser retornado.