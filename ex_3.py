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

def ladderLength(beginWord, endWord, wordList):
    # Converte a lista de palavras em um conjunto para busca
    wordSet = set(wordList)
        
    # Se a palavra final não estiver no conjunto, não há caminho possível
    if endWord not in wordSet:
        return 0
    
    # Inicia a fila e o comprimento da transformação
    queue = [(beginWord, 1)]  # (palavra atual, comprimento da transformação)    
    
    while queue:
        current_word, length = queue.pop(0)
        print(current_word, length)
        
        # Se a palavra atual for igual à palavra final, retorna o comprimento
        if current_word == endWord:
            return length
        
        # Itera sobre cada letra da palavra atual
        for i in range(len(current_word)):            
            for c in 'abcdefghijklmnopqrstuvwxyz':                
                # Cria uma nova palavra substituindo uma letra
                new_word = current_word[:i] + c + current_word[i+1:]
               
                # Se a nova palavra estiver no conjunto de palavras e não foi buscada ainda
                if new_word in wordSet:
                    queue.append((new_word, length + 1))
                    wordSet.remove(new_word)  # Remove para evitar buscas futuras
    
    return 0  # Retorna 0 se não houver caminho possível

print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # Saída: 5
print(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))  # Saída: 0 (não há caminho possível)