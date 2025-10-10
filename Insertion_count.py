import time
import random
from typing import List, Dict
from tabulate import tabulate

def execucaoIn(lista: List[int]) -> Dict[str, object]:
   
    comparacoes = 0
    movimentos = 0
    arr = lista[:] 
    inicio = time.perf_counter()

    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            comparacoes += 1
            arr[j + 1] = arr[j]
            movimentos += 1
            j -= 1
        if j >= 0:
            comparacoes += 1
        arr[j + 1] = chave

    fim = time.perf_counter()
    return {
        "comparacoes": comparacoes,
        "movimentos": movimentos,
        "tempo": fim - inicio,
        "complexidade": "O(n²) — O(n) melhor (ordenado)"
    }

def comparacao():
    casos = {
        "Ordenado": list(range(1, 21)),
        "Inverso": list(range(20, 0, -1)),
        "Aleatório": random.sample(range(1, 1000), 20)
    }

    resultados = []
    for nome, lista in casos.items():
        resultados.append(["Insertion Sort", nome, *execucaoIn(lista).values()])

    headers = ["Algoritmo", "Caso", "Comparações", "Movimentos", "Tempo (s)", "Complexidade Teórica"]
    print("\n===== Tabela comparativa InsertionSort =====\n")
    print(tabulate(resultados, headers=headers, floatfmt=".8f", tablefmt="grid"))

if __name__ == "__main__":
    comparacao()
