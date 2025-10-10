import random
import time
from typing import List, Dict
from tabulate import tabulate 

qscomp = 0
quickmove = 0

def quick_count(lista: List[int]) -> List[int]:
    global qscomp
    global quickmove
    n = len(lista)
    if n <= 1:
        return lista[:]
    pivo = lista[n // 2]
    menores, iguais, maiores = [], [], []
    for x in lista:
        qscomp += 1
        if x < pivo:
            menores.append(x)
            quickmove += 1
        elif x == pivo:
            iguais.append(x)
            quickmove += 1
        else:
            maiores.append(x)
            quickmove += 1
    left = quick_count(menores)
    right = quick_count(maiores)
    quickmove += len(iguais)
    return left + iguais + right

def execucaoQ(lista: List[int]) -> Dict[str, object]:
    global qscomp
    global quickmove
    qscomp = quickmove = 0
    ini = time.perf_counter()
    quick_count(lista)
    fim = time.perf_counter()
    return {
        "comparacoes": qscomp,
        "movimentos": quickmove,
        "tempo": fim - ini,
        "complexidade": "O(n log n) média — O(n²) pior"
    }

compmerge = 0
mergexerox = 0

def merge_count(lista: List[int]) -> List[int]:
    global compmerge
    global mergexerox
    if len(lista) <= 1:
        return lista[:]
    meio = len(lista)//2
    esq = merge_count(lista[:meio])
    dir = merge_count(lista[meio:])
    i = j = 0
    resultado = []
    while i < len(esq) and j < len(dir):
        compmerge += 1
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            mergexerox += 1
            i += 1
        else:
            resultado.append(dir[j])
            mergexerox += 1
            j += 1
    while i < len(esq):
        resultado.append(esq[i])
        mergexerox += 1
        i += 1
    while j < len(dir):
        resultado.append(dir[j])
        mergexerox += 1
        j += 1
    return resultado

def execucaoM(lista: List[int]) -> Dict[str, object]:
    global compmerge
    global mergexerox
    compmerge = mergexerox = 0
    ini = time.perf_counter()
    merge_count(lista)
    fim = time.perf_counter()
    return {
        "comparacoes": compmerge,
        "movimentos": mergexerox,
        "tempo": fim - ini,
        "complexidade": "O(n log n) em todos os casos"
    }


def execucaoIn(lista: List[int]) -> Dict[str, object]:
    comparacoes = 0
    deslocamentos = 0
    arr = lista[:]
    ini = time.perf_counter()
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            comparacoes += 1
            arr[j + 1] = arr[j]
            deslocamentos += 1
            j -= 1
        if j >= 0:
            comparacoes += 1
        arr[j + 1] = chave
    fim = time.perf_counter()
    return {
        "comparacoes": comparacoes,
        "movimentos": deslocamentos,
        "tempo": fim - ini,
        "complexidade": "O(n²) — O(n) melhor (ordenado)"
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
        resultados.append(["Merge Sort", nome, *execucaoM(lista).values()])
        resultados.append(["Insertion Sort", nome, *execucaoIn(lista).values()])

    headers = ["Algoritmo", "Caso", "Comparações", "Movimentos", "Tempo (s)", "Complexidade Teórica"]
    print("\n===== Tabela comparativa dos alogoritmos de ordenação =====\n")
    print(tabulate(resultados, headers=headers, floatfmt=".8f", tablefmt="grid"))  

if __name__ == "__main__":
    comparar()
