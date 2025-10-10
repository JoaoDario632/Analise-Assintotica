import time
import random
from typing import List, Dict
from tabulate import tabulate

# ================== QUICK SORT =====================
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
    movimentos_qs += len(iguais)  # concatenação

    return left + iguais + right


def execucaoQ(lista: List[int]) -> Dict[str, object]:
    """
    Executa QuickSort e retorna métricas padronizadas:
    - comparações
    - movimentos
    - tempo
    - complexidade teórica
    """
    global comparacoes_qs, movimentos_qs
    comparacoes_qs = 0
    movimentos_qs = 0
    inicio = time.perf_counter()
    quick_count(lista)
    fim = time.perf_counter()

    return {
        "comparacoes": comparacoes_qs,
        "movimentos": movimentos_qs,
        "tempo": fim - inicio,
        "complexidade": "O(n log n) média — O(n²) pior"
    }

def comparacao():
    casos = {
        "Ordenado": list(range(1, 21)),
        "Inverso": list(range(20, 0, -1)),
        "Aleatório": random.sample(range(1, 1000), 20)
    }

    resultados = []
    for nome, lista in casos.items():
        resultados.append(["Quick Sort", nome, *execucaoQ(lista).values()])

    headers = ["Algoritmo", "Caso", "Comparações", "Movimentos", "Tempo (s)", "Complexidade Teórica"]
    print("\n===== Tabela comparativa QuickSort =====\n")
    print(tabulate(resultados, headers=headers, floatfmt=".8f", tablefmt="grid"))


def analise_teorica(lista: List[int], mostrar_tabela: bool = False) -> Dict[str, object]:
    """
    Executa QuickSort e, se mostrar_tabela=True,
    imprime a tabela de contagem e os cálculos de f(n).
    """
    global comparacoes_qs, movimentos_qs
    comparacoes_qs = 0
    movimentos_qs = 0
    inicio = time.perf_counter()
    ordenada = quick_count(lista)
    fim = time.perf_counter()

    resultado = {
        "ordenada": ordenada,
        "comparacoes": comparacoes_qs,
        "movimentos": movimentos_qs,
        "tempo_s": fim - inicio,
    }

    if mostrar_tabela:
        # ===== TABELA DE CONTAGEM =====
        headers = ["Operação / Linha de Código", "Médio", "Melhor (pivô ~ n/2)", "Pior (pivô extremo)"]
        tabela = [
            ["comparacoes_qs = 0", "1", "1", "1"],
            ["movimentos_qs = 0", "1", "1", "1"],
            ["n = len(lista)", "2", "2", "2"],
            ["if n <= 1:", "1", "1", "1"],
            ["return lista[:]", "2", "2", "2"],
            ["pivo = lista[n // 2]", "3", "3", "3"],
            ["menores = []", "1", "1", "1"],
            ["iguais = []", "1", "1", "1"],
            ["maiores = []", "1", "1", "1"],
            ["for x in lista:", "1+n+(n-1)", "1+n+(n-1)", "1+n+(n-1)"],
            ["comparacoes_qs += 1", "2n", "2n", "2n"],
            ["if x < pivo:", "n", "n", "n"],
            ["menores.append(x)", "n", "n", "n"],
            ["movimentos_qs += 1", "2n", "2n", "2n"],
            ["elif x == pivo:", "n", "n", "n"],
            ["iguais.append(x)", "n", "n", "n"],
            ["movimentos_qs += 1", "2n", "2n", "2n"],
            ["else:", "n", "n", "n"],
            ["maiores.append(x)", "n", "n", "n"],
            ["movimentos_qs += 1", "2n", "2n", "2n"],
            ["left = quick_count(menores)", "f(k)+1", "f(n/2)+1", "f(1)"],
            ["right = quick_count(maiores)", "f(n-k)+1", "f(n/2)+1", "f(n-1)"],
            ["movimentos_qs += len(iguais)", "3", "3", "3"],
            ["return left + iguais + right", "3", "3", "3"],
        ]
        print("\n===== Tabela de Contagem do Quick Sort =====\n")
        print(tabulate(tabela, headers=headers, tablefmt="grid"))

        # ===== CÁLCULOS DA FUNÇÃO f(n) =====
        print("\n===== Cálculo da Função de Complexidade f(n) =====\n")
        print("f(n) = 21 + 15n + f(k) + f(n-k)")

        print("\n🔹 Melhor caso: k = n/2 (divisão equilibrada)")
        print("f(n) = 21 + 15n + 2f(n/2)")
        print("Expansão → f(n) = 21 + 15n·log₂n + n·log₂n → Ω(n log n)")

        print("\n🔹 Pior caso: k = 1 (pivô sempre menor/maior)")
        print("f(n) = 21 + 15n + f(1) + f(n-1)")
        print("Expansão da série → f(n) ≈ 7.5n² + 35.5n + 7 → O(n²)")

        print("\n🔹 Caso médio: k ≈ n/2 (divisão balanceada em média)")
        print("f(n) = 21 + 15n + 2f(n/2)")
        print("Expansão → f(n) = 21 + 15n·log₂n + n·log₂n → Θ(n log n)")

    return resultado


# ================== TESTE LOCAL =====================
if __name__ == "__main__":
    comparacao()
    lista_ordenada = list(range(1, 21))
    lista_inversa = list(range(20, 0, -1))
    lista_aleatoria = random.sample(range(1, 100), 20)

    # Exemplo com tabela teórica
    print("\n===== Análise Teórica (com tabela) =====")
    analise_teorica(lista_aleatoria, mostrar_tabela=True)