As estruturas de dados impactam diretamente o desempenho de um programa, influenciando o tempo de execução, o uso de memória e a escalabilidade.

Impacto das Estruturas de Dados no Desempenho

Eficiência no acesso e busca de dados:
Um array (lista) permite acesso rápido a elementos via índice (O(1)).
Uma lista encadeada pode exigir O(n) para busca, pois precisa percorrer os elementos sequencialmente.
Eficiência na inserção e remoção:
Em um array, a inserção no meio pode ser O(n) devido à necessidade de realocar elementos.
Em uma árvore balanceada (como AVL), operações de inserção e remoção podem ser O(log n).
Uso otimizado de memória:
Estruturas dinâmicas como listas encadeadas evitam desperdício de memória, pois alocam espaço conforme necessário.
Estruturas como tabelas hash evitam buscas lineares repetitivas e reduzem o tempo de processamento.

Exemplo Prático: Código sem tratamento de estrutura de dados vs. Código otimizado
O código abaixo compara duas abordagens para buscar um número em uma lista de 1 milhão de elementos.

1 - Código sem otimização (busca linear em lista comum, O(n))
2 - Código otimizado (busca em conjunto, O(1) em média)

Criarei um arquivo comparacao_estruturas.py demonstrando essa diferença.
