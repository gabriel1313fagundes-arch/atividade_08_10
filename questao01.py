# 1) Crie uma lista A com 6 inteiros e execute, nesta ordem.
## a) atribua os valores [1, 0, 5, -2, -5, 7];

A = [1, 0, 5, -2, -5, 7]

# b) guarde em uma variavel simples a soma de A[0], A[1] e A[5] e mostre o resultado;

soma = A[0] + A[1] + A[5]
print("Resultado da soma:", soma)

#c) modifique a posição 4, atribuindo o valor 100;

A[4] = 100

# d) mostre cada elemento de A, um por linha..
## Resultado esperado: a soma mostrada é 8, e a lista final impressa é 1, 0, 5, -2, 100, 7.
for i in range(6):
 print(A[i])
