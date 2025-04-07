# Exercício 3: Word Ladder (Escada de Palavras)

# - Descrição: Neste exercício, você deve implementar uma função que encontra o comprimento do caminho mais curto de transformação de uma palavra inicial para uma palavra final, seguindo as regras abaixo:
#   1. A cada transformação, apenas uma letra pode ser alterada.
#   2. Cada palavra intermediária deve existir no dicionário fornecido.
 
#   A entrada do exercício será composta por duas palavras de mesma dimensão e uma lista de palavras. Sua tarefa é encontrar a sequência mais curta de transformações, ou retornar 0 caso não seja possível.
 
# Exemplo:
# ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])  
# # Saída: 5 ("hit" -> "hot" -> "dot" -> "dog" -> "cog")

# ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])  
# # Saída: 0 (não há caminho possível)