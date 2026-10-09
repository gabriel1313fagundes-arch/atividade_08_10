# Cria dois vetores vazios e inicializa o produto escalar com zero
x = []
y = []
produto = 0

# Lê os 5 números reais do primeiro vetor (X)
for i in range(5):
    num = float(input(f"Digite o {i + 1}º número do vetor X: "))
    x.append(num)  # Adiciona o número ao vetor X

# Lê os 5 números reais do segundo vetor (Y)
for i in range(5):
    num = float(input(f"Digite o {i + 1}º número do vetor Y: "))
    y.append(num)  # Adiciona o número ao vetor Y

# Calcula o produto escalar multiplicando os elementos
# que estão nas mesmas posições e somando os resultados
for i in range(5):
    produto += x[i] * y[i]

# Exibe os dois vetores na tela
print("Vetor X:", x)
print("Vetor Y:", y)

# Exibe o resultado do produto escalar
print("Produto escalar:", produto)