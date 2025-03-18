# Exemplo de Alocação Dinâmica em Python usando Listas

def exemplo_alocacao_dinamica():
    """
    Demonstra a alocação dinâmica em Python utilizando listas.
    As listas podem crescer ou diminuir de tamanho durante a execução.
    """

    # Inicialmente, a lista está vazia
    dados = []
    print(f"Lista inicial: {dados} (Tamanho: {len(dados)})")

    # Adicionando elementos dinamicamente
    for i in range(5):
        novo_elemento = f"Elemento {i+1}"
        dados.append(novo_elemento)
        print(f"Lista após adicionar '{novo_elemento}': {dados} (Tamanho: {len(dados)})")

    # Removendo elementos dinamicamente
    while dados:
        elemento_removido = dados.pop()
        print(f"Lista após remover '{elemento_removido}': {dados} (Tamanho: {len(dados)})")

    print("Lista final: {}".format(dados))

if __name__ == "__main__":
    exemplo_alocacao_dinamica()
