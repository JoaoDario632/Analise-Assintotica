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

lista2 = [10, 7, 8, 9, 1, 5]
inicio = time.time()
resultado = quick(lista2)
fim = time.time()

print("\n######## Quick Sort ########")
print("Lista ordenada:", resultado)
print(f"Comparações: {comparacoes}")
print(f"Tempo de execução: {fim - inicio:.6f} segundos")
