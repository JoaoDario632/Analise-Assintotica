import random
import time
from typing import List, Dict
from tabulate import tabulate
from typing import List, Tuple

def quick_count(lista: List[int]) -> Tuple[List[int], int, int]:
    n = len(lista)
    if n <= 1:
        return lista[:], 0, 0

    pivo = lista[n // 2]
    menores, iguais, maiores = [], [], []

    comp = mov = 0

    for x in lista:
        comp += 1
        if x < pivo:
            menores.append(x)
            mov += 1
        elif x == pivo:
            iguais.append(x)
            mov += 1
        else:
            maiores.append(x)
            mov += 1

    left, comp_left, mov_left = quick_count(menores)
    right, comp_right, mov_right = quick_count(maiores)

    comp += comp_left + comp_right
    mov += mov_left + mov_right + len(iguais)  

    return left + iguais + right, comp, mov


def execucaoQ(lista: List[int]) -> Dict[str, object]:
    """Executa QuickSort e retorna métricas"""
    ini = time.perf_counter()
    _, comp, mov = quick_count(lista)
    fim = time.perf_counter()
    return {
        "comparacoes": comp,
        "movimentos": mov,
        "tempo": fim - ini,
        "complexidade": "O(n log n) média — O(n²) pior"
    }

def comparar():
    casos = {
        "Ordenado": list(range(1, 201)),
        "Inverso": list(range(200, 0, -1)),
        "Aleatório": random.sample(range(1, 10000), 200)
    }

    resultados = []
    for nome, lista in casos.items():
        resultados.append(["Quick Sort", nome, *execucaoQ(lista).values()])

    headers = ["Algoritmo", "Caso", "Comparações", "Movimentos", "Tempo (s)", "Complexidade Teórica"]
    print("\n===== Tabela comparativa QuickSort =====\n")
    print(tabulate(resultados, headers=headers, floatfmt=".8f", tablefmt="grid"))  

if __name__ == "__main__":
    comparar()
