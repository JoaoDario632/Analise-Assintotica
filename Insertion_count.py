import time
import random
from typing import List, Dict
from tabulate import tabulate

# ================== INSERTION SORT =====================
def execucaoIn(lista: List[int]) -> Dict[str, object]:
    """
    Executa Insertion Sort medindo comparações, movimentos e tempo real.
    """
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


def insertion_count(lista: List[int], mostrar_tabela: bool = False) -> Dict[str, object]:
    """
    Insertion Sort com contadores de operações + tabela teórica.
    Retorna dicionário com lista ordenada, comparações, deslocamentos e tempo em segundos.
    Se mostrar_tabela=True, exibe a tabela de contagem teórica e os cálculos de f(n).
    """
    comparacoes = 0
    deslocamentos = 0
    n = len(lista)
    arr = lista[:]
    inicio = time.perf_counter()

    for i in range(1, n):
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
    resultado = {
        "ordenada": arr,
        "comparacoes": comparacoes,
        "deslocamentos": deslocamentos,
        "tempo_s": fim - inicio,
    }

    if mostrar_tabela:
        # ===== TABELA DE CONTAGEM =====
        headers = ["Instrução", "Médio (Aleatório)", "Melhor (Ordenada)", "Pior (Invertida)"]
        tabela = [
            ["comparacoes = 0", "1", "1", "1"],
            ["deslocamentos = 0", "1", "1", "1"],
            ["n = len(lista)", "2", "2", "2"],
            ["arr = lista[:]", "n+1", "n+1", "n+1"],
            ["inicio = time.perf_counter()", "2", "2", "2"],
            ["for i in range(1,n)", "1 + n(n-1)", "1 + n(n-1)", "1 + n(n-1)"],
            ["chave = arr[i]", "2(n-1)", "2(n-1)", "2(n-1)"],
            ["j = i-1", "2(n-1)", "2(n-1)", "2(n-1)"],
            ["while j>=0 and arr[j]>chave", "4(n(n-1)k/2 + (n-1))", "4(n-1)", "4(n(n-1)/2 + (n-1))"],
            ["comparacoes += 1", "2n(n-1)k/2", "0", "2n(n-1)/2"],
            ["arr[j+1] = arr[j]", "4n(n-1)k/2", "0", "4n(n-1)/2"],
            ["deslocamentos += 1", "2n(n-1)k/2", "0", "2n(n-1)/2"],
            ["j -= 1", "2n(n-1)k/2", "0", "2n(n-1)/2"],
            ["if j >= 0", "n-1", "n-1", "n-1"],
            ["comparacoes += 1", "n-1", "n-1", "n-1"],
            ["arr[j+1] = chave", "3(n-1)", "3(n-1)", "3(n-1)"],
            ["fim = time.perf_counter()", "1", "1", "1"],
            ["return {...}", "5", "5", "5"]
        ]
        print("\n===== Tabela de Contagem do Insertion Sort =====\n")
        print(tabulate(tabela, headers=headers, tablefmt="grid"))

        # ===== CÁLCULOS DA FUNÇÃO f(n) =====
        print("\n===== Cálculo da Função de Complexidade f(n) =====\n")
        print("f(n) = 1 + 1 + 2 + n+1 + 2 + 1+n(n-1) + 2(n-1) + 2(n-1) "
              "+ 4(n(n-1)k/2 + (n-1)) + 2n(n-1)k/2 + 4n(n-1)k/2 "
              "+ 2n(n-1)k/2 + 2n(n-1)k/2 + n-1 + n-1 + 3(n-1) + 1 + 5")
        print("\nSimplificação → f(n) = 16n + 7n²k - 7nk")
        print("\n🔹 Melhor caso (k = 0): f(n) = 16n ∈ Ω(n)")
        print("🔹 Pior caso   (k = 1): f(n) = 7n² + 9n ∈ O(n²)")
        print("🔹 Médio caso (k = 0,5): f(n) = 3,5n² + 12,5n ∈ Θ(n²)")

    return resultado


def comparacao():
    """
    Executa o Insertion Sort em três casos (ordenado, inverso e aleatório),
    exibindo uma tabela comparativa de desempenho real.
    """
    casos = {
        "Ordenado": list(range(1, 21)),
        "Inverso": list(range(20, 0, -1)),
        "Aleatório": random.sample(range(1, 1000), 20)
    }

    resultados = []
    for nome, lista in casos.items():
        resultados.append(["Insertion Sort", nome, *execucaoIn(lista).values()])

    headers = ["Algoritmo", "Caso", "Comparações", "Movimentos", "Tempo (s)", "Complexidade Teórica"]
    print("\n===== Tabela comparativa Insertion Sort =====\n")
    print(tabulate(resultados, headers=headers, floatfmt=".8f", tablefmt="grid"))


if __name__ == "__main__":
    comparacao()
    # Exemplo mostrando a tabela teórica e os cálculos
    print("\n===== Demonstração com Tabela Teórica =====")
    lista_exemplo = random.sample(range(1, 100), 10)
    insertion_count(lista_exemplo, mostrar_tabela=True)