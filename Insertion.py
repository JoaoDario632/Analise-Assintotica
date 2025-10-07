import time

def insertion(lista):
    comparacoes = 0
    trocas = 0
    inicio = time.time()

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            comparacoes += 1
            lista[j + 1] = lista[j]
            trocas += 1
            j -= 1
        lista[j + 1] = chave

    fim = time.time()

    print("\n#### Insertion Sort ####")
    print("Lista ordenada:", lista)
    print(f"Comparações: {comparacoes}")
    print(f"Trocas: {trocas}")
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")

# Exemplo:
lista1 = [5, 3, 8, 4, 2]
insertion(lista1)
