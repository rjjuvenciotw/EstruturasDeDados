# Exemplo de alocação estática em Python

# Definição de um array com tamanho fixo
numeros = [0] * 5  # Criação de um array de tamanho fixo (5 posições)

# Atribuindo valores
numeros[0] = 10
numeros[1] = 20
numeros[2] = 30
numeros[3] = 40
numeros[4] = 50

# Exibindo os valores
print("Valores armazenados no array (alocação estática):")
for i in range(5):
    print(f"Posição {i}: {numeros[i]}")
