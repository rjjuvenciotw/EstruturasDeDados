class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.itens[0]
        else:
            return None

    def is_empty(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)


# Simulador de fila de atendimento bancário
fila_banco = Fila()

# Clientes chegam e pegam senhas
fila_banco.enqueue("Cliente 1")
fila_banco.enqueue("Cliente 2")
fila_banco.enqueue("Cliente 3")

# Atendimento dos clientes
print("Próximo cliente:", fila_banco.dequeue())  # Saída: Cliente 1
print("Próximo cliente:", fila_banco.dequeue())  # Saída: Cliente 2

# Novo cliente chega
fila_banco.enqueue("Cliente 4")

# Atendimento do próximo cliente
print("Próximo cliente:", fila_banco.dequeue())  # Saída: Cliente 3

# Impressão da fila restante
print("Fila restante:", fila_banco.itens)  # Saída: ['Cliente 4']
