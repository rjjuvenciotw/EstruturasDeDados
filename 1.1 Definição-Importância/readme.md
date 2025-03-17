### Impacto das Estruturas de Dados no Desempenho

As estruturas de dados influenciam diretamente o desempenho de um programa, afetando o tempo de execução, o uso de memória e a escalabilidade. A escolha correta pode tornar um algoritmo mais eficiente e otimizado.

## Eficiência no Acesso e Busca de Dados
Array (Lista): Permite acesso rápido a elementos via índice (O(1)).
Lista Encadeada: Pode exigir O(n) para busca, pois é necessário percorrer os elementos sequencialmente.
##Eficiência na Inserção e Remoção
Array: Inserir ou remover elementos no meio pode ser O(n) devido à realocação necessária.
Árvore Balanceada (como AVL): Operações de inserção e remoção podem ser feitas em O(log n), tornando-as mais eficientes.
Uso Otimizado de Memória
Listas Encadeadas: Alocam espaço dinamicamente, evitando desperdício de memória.
Tabelas Hash: Eliminam buscas lineares repetitivas, reduzindo o tempo de processamento.
##Exemplo Prático: Código Não Otimizado vs. Código Otimizado
O código abaixo compara duas abordagens para buscar um número em uma lista de 1 milhão de elementos:

#Código sem otimização: Utiliza busca linear em uma lista comum (O(n)).
#Código otimizado: Utiliza um conjunto (set), reduzindo o tempo de busca para O(1) em média.
