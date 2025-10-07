import time

comparacoes_ms = 0

def merge(lista):
    global comparacoes_ms
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge(esquerda)
        merge(direita)

        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            comparacoes_ms += 1
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    return lista

lista3 = [38, 27, 43, 3, 9, 82, 10]
inicio = time.time()
resultado = merge(lista3)
fim = time.time()

print("\n################ Merge Sort #################")
print("Lista ordenada:", resultado)
print(f"Comparações: {comparacoes_ms}")
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
