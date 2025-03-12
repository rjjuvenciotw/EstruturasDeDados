import time

# Criando uma grande lista de números
numeros = list(range(1, 1_000_001))  # Lista de 1 milhão de elementos
procurado = 999_999  # Número a ser buscado

# --- MÉTODO SEM OTIMIZAÇÃO (Busca Linear) ---
inicio = time.time()
encontrado = procurado in numeros  # Busca na lista (O(n))
fim = time.time()
print(f"Busca em lista comum: {fim - inicio:.6f} segundos")

# --- MÉTODO OTIMIZADO (Uso de Conjunto) ---
numeros_set = set(numeros)  # Convertendo para conjunto (O(1) para busca)
inicio = time.time()
encontrado = procurado in numeros_set  # Busca otimizada
fim = time.time()
print(f"Busca em conjunto: {fim - inicio:.6f} segundos")