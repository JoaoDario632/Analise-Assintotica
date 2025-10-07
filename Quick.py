import time

comparacoes = 0

def quick(lista):
    global comparacoes
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[len(lista) // 2]
        menores, iguais, maiores = [], [], []

        for x in lista:
            comparacoes += 1
            if x < pivo:
                menores.append(x)
            elif x == pivo:
                iguais.append(x)
            else:
                maiores.append(x)

        return quick(menores) + iguais + quick(maiores)

lista2 = [10, 7, 8, 9, 1, 5,7,23,32,34,22,54,45,56,57,78,12,3,6,7,9,0,2,567,123,124,145,1234,543,678,163,]
inicio = time.time()
resultado = quick(lista2)
fim = time.time()

print("\n######## Quick Sort ########")
print("Lista ordenada:", resultado)
print(f"Comparações: {comparacoes}")
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
