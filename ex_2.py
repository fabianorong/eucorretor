# Exercício 2: Mesclar Intervalos

# - Descrição: Dada uma lista de intervalos, você deve implementar uma função que mescla os intervalos sobrepostos. Cada intervalo é representado por um par de números [início, fim]. Caso dois intervalos se sobreponham, eles devem ser combinados em um único intervalo.

# Exemplo:
# merge_intervals([[1,3], [2,6], [8,10], [15,18]])  
# # Saída: [[1, 6], [8, 10], [15, 18]]

# merge_intervals([[1,4], [4,5]])  
# # Saída: [[1, 5]]


def merge_intervals(intervals):
    # Se a lista estiver vazia, retorna uma lista vazia
    if not intervals:
        return []

    # Ordena os intervalos com base no início de cada intervalo
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]  # Começa com o primeiro intervalo

    for current in intervals[1:]:
        last_merged = merged[-1]

        # Verifica se há sobreposição entre os intervalos
        if current[0] <= last_merged[1]:
            # Mescla os intervalos atual e o último mesclado
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Caso contrário, adiciona o intervalo atual à lista mesclada
            merged.append(current)

    return merged

print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Saída: [[1, 6], [8, 10], [15, 18]]
print(merge_intervals([[1, 4], [4, 5]]))  # Saída: [[1, 5]]