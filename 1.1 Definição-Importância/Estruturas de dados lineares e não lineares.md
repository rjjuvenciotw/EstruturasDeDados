# Diferença entre Estruturas de Dados Lineares e Não Lineares

A principal diferença entre estruturas de dados lineares e não lineares está na maneira como os elementos são organizados e acessados.

## Estruturas de Dados Lineares
Nas estruturas lineares, os elementos são organizados de forma sequencial, ou seja, cada elemento tem um predecessor e/ou sucessor, permitindo um acesso mais previsível.

### Exemplos de Estruturas Lineares:

- **Array (Vetor/Listas)** → Uma sequência de elementos armazenados em posições contíguas na memória.  
  **Exemplo**: Uma lista de nomes `["Ana", "Bruno", "Carlos"]`.

- **Lista Encadeada** → Elementos conectados por ponteiros, onde cada nó contém um valor e uma referência para o próximo nó.

- **Fila (Queue)** → Segue a regra **FIFO** (*First In, First Out*), onde o primeiro elemento inserido é o primeiro a sair.  
  **Exemplo**: Fila de impressão em uma impressora.

- **Pilha (Stack)** → Segue a regra **LIFO** (*Last In, First Out*), onde o último elemento inserido é o primeiro a ser removido.  
  **Exemplo**: Pilha de pratos em um restaurante.

---

## Estruturas de Dados Não Lineares
Nessas estruturas, os elementos são organizados de maneira hierárquica ou interconectada de forma mais complexa, sem uma sequência fixa.

### Exemplos de Estruturas Não Lineares:

- **Árvores (Tree)** → Uma estrutura hierárquica composta por nós, onde cada nó pode ter múltiplos filhos, mas um único pai.  
  **Exemplo**: Árvore genealógica ou estrutura de diretórios de um sistema operacional.

- **Grafos (Graph)** → Uma coleção de nós (*vértices*) conectados por arestas, podendo ser direcionado ou não.  
  **Exemplo**: Rede social, onde pessoas são nós e conexões entre elas são arestas.

- **Tabelas Hash (Hash Table)** → Usa uma função de hash para mapear chaves a valores, permitindo acesso rápido aos dados.  
  **Exemplo**: Um dicionário de palavras e definições em Python `{ 'chave': 'valor' }`.

---

## Resumo

| Tipo         | Organização                        | Exemplos                          |
|-------------|--------------------------------|--------------------------------|
| **Linear**  | Sequencial                     | Arrays, Listas Encadeadas, Filas, Pilhas |
| **Não Linear** | Hierárquica ou interconectada | Árvores, Grafos, Hash Tables |

Compreender a diferença entre essas estruturas é essencial para escolher a mais adequada ao seu projeto e otimizar o desempenho dos algoritmos utilizados.

