from No import No

class Lista:
    def __init__(self):
        self.inicio = None  


    def bubble_sort(lista):
     tamanho_lista = len(lista)
     passadas = 0
     for i in range(tamanho_lista):
        troca = True
        passadas += 1
        for j in range(0, tamanho_lista - i - 1):
         if lista[j] > lista[j+1]:
           lista[j], lista[j+1] = lista[j+1], lista[j]
         troca = True
         if troca:
          print("Troca!")
         else:
          break  
        return lista

   

