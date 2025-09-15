#  QuickSort é um dos algoritmos de ordenação mais eficientes e populares da ciência da computação.
# o algoritmo organiza uma lista de elementos quebrando-a em sub-listas menores e ordenando-as recursivamente.

# Possui 2 conceitos: Pivô e a Partição:

#Escolha do Pivô: Primeiro, um elemento da lista é selecionado para ser o "pivô". 
# A escolha do pivô pode variar; pode ser o primeiro, o último, um elemento do meio ou um elemento aleatório da lista. 
# A estratégia de escolha do pivô pode impactar o desempenho do algoritmo.

#Particionamento: Após a escolha do pivô, a lista é rearranjada. 
# Todos os elementos menores que o pivô são movidos para a sua esquerda, e todos os elementos maiores são movidos para a sua direita. 
# Os elementos iguais podem ficar em qualquer um dos lados. Ao final deste processo, 
# o pivô estará em sua posição final e correta na lista ordenada.




# IMPLEMENTAÇÃO: 

def partition(array, low, high):

    pivot = array[high]    

    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    

    return i + 1

def quick_sort(array, low, high):

    if low < high:

        pi = partition(array, low, high)
        
   
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


data = [7, 2, 1, 6, 8, 5, 3, 4]
print("Array Desordenado:")
print(data)

size = len(data)
quick_sort(data, 0, size - 1)

print("Array Ordenado:")
print(data)