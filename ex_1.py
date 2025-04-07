# Exercício 1: Encontrar o Primeiro Caractere Não Repetido em uma String

# - Descrição: Neste exercício, você deve implementar uma função que encontra o primeiro caractere que não se repete em uma string. Caso todos os caracteres sejam repetidos, a função deve retornar -1.
 
# Exemplo:
# firstUniqChar("abacabad")  # Saída: 3 ('c')
# firstUniqChar("aaabb")      # Saída: -1 (não há caracteres não repetidos)

# Para realizacao do exercicio foi considerada que o input do usuario poderia conter espaços em brancos, letras maiusculas e minusculas, e que o retorno do primeiro caractere não repetido deveria ser sem considerar os espaços em brancos e sem considerar se a letra é maiúscula ou minúscula.

def firstUniqChar(s):
    # Cria um dicionário para armazenar a contagem de cada caractere
    char_count = {}
    
    # Conta a ocorrência de cada caractere na string
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Encontra o primeiro caractere que não se repete
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    # Se não houver caracteres não repetidos, retorna -1
    return -1

while True:
    # Solicita ao usuário que digite uma string
    # O método replace() remove os espaços em branco da string
    # O método lower() converte a string para minúsculas
    user_input = input("Digite a string: ").replace(" ", "").lower()    
    result = firstUniqChar(user_input)

    if result != -1:
        print(f"O primeiro caractere não repetido é '{user_input[result]}' na posição {result+1}.")
    else:
        print("Não há caracteres não repetidos na string.")
    
    # Pergunta ao usuário se deseja repetir
    # O método strip() remove espaços em branco do início e do fim da string
    # O método lower() converte a string para minúsculas
    repetir = input("Deseja digitar uma nova string? (s/n): ").strip().lower()
    
    # Verifica se o usuário deseja repetir
    if repetir != 's':
        print("Encerrando o programa.")
        break

    


