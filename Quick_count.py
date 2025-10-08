import time
import random
from typing import List, Dict

comparacoes_qs = 0
movimentos_qs = 0  # conta inserções em listas auxiliares (append)


def quick_count(lista: List[int]) -> List[int]:
    """
    Quick Sort recursivo (não in-place) com contadores globais.
    Retorna lista ordenada. Atualiza comparacoes_qs e movimentos_qs.
    """
    global comparacoes_qs, movimentos_qs
    n = len(lista)
    if n <= 1:
        return lista[:]

    pivo = lista[n // 2]
    menores: List[int] = []
    iguais: List[int] = []
    maiores: List[int] = []

    for x in lista:
        comparacoes_qs += 1
        if x < pivo:
            menores.append(x)
            movimentos_qs += 1
        elif x == pivo:
            iguais.append(x)
            movimentos_qs += 1
        else:
            maiores.append(x)
            movimentos_qs += 1

    left = quick_count(menores)
    right = quick_count(maiores)
    # concatenação também apresenta custo de cópia; contabilizamos no movimentos_qs pela soma dos tamanhos
    movimentos_qs += len(iguais)
    return left + iguais + right


def run_and_report(lista: List[int]) -> Dict[str, object]:
    global comparacoes_qs, movimentos_qs
    comparacoes_qs = 0
    movimentos_qs = 0
    inicio = time.perf_counter()
    ordenada = quick_count(lista)
    fim = time.perf_counter()
    return {
        "ordenada": ordenada,
        "comparacoes": comparacoes_qs,
        "movimentos": movimentos_qs,
        "tempo_s": fim - inicio,
    }


if __name__ == "__main__":
    # Exemplos: ordenado (pior para algumas implementações), inverso, aleatório
    lista_ordenada = list(range(1, 201))
    lista_inversa = list(range(200, 0, -1))
    lista_aleatoria = random.sample(range(1, 10000), 200)

    for nome, lst in (
        ("ordenado", lista_ordenada),
        ("inverso", lista_inversa),
        ("aleatorio", lista_aleatoria),
    ):
        resultado = run_and_report(lst)
        print(f"\n#### Quick Sort — caso: {nome} ####")
        print(f"Comparações (particionamento): {resultado['comparacoes']}")
        print(f"Movimentos (inserções/concatenações): {resultado['movimentos']}")
        print(f"Tempo: {resultado['tempo_s']:.8f} s")
