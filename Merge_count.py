import time
import random
from typing import List, Dict
from tabulate import tabulate

# ================== MERGE SORT =====================
compporElemento = 0
copias_ms = 0

def merge_count(lista: List[int]) -> List[int]:
    """
    Merge Sort recursivo com contadores globais.
    Atualiza compporElemento (comparações entre elementos)
    e copias_ms (escritas durante o merge).
    """
    global compporElemento, CopiasMG
    if len(lista) <= 1:
        return lista[:]

    meio = len(lista) // 2
    esquerda = merge_count(lista[:meio])
    direita = merge_count(lista[meio:])

    i = j = 0
    resultado: List[int] = []

    # processo de intercalação (merge)
    while i < len(esquerda) and j < len(direita):
        compporElemento += 1
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            CopiasMG += 1
            i += 1
        else:
            resultado.append(direita[j])
            CopiasMG += 1
            j += 1

    # adiciona o restante das listas
    while i < len(esquerda):
        resultado.append(esquerda[i])
        CopiasMG += 1
        i += 1
    while j < len(direita):
        resultado.append(direita[j])
        CopiasMG += 1
        j += 1

    return resultado


def execucaoM(lista: List[int]) -> Dict[str, object]:
    """
    Executa Merge Sort e retorna métricas padronizadas:
    - comparações
    - movimentos (cópias)
    - tempo
    - complexidade teórica
    """
    global compporElemento, CopiasMG
    compporElemento = 0
    CopiasMG = 0
    inicio = time.perf_counter()
    merge_count(lista)
    fim = time.perf_counter()

    return {
        "comparacoes": compporElemento,
        "movimentos": CopiasMG,
        "tempo": fim - inicio,
        "complexidade": "O(n log n) em todos os casos"
    }

def comparacao():
    casos = {
        "Ordenado": list(range(1, 21)),
        "Inverso": list(range(20, 0, -1)),
        "Aleatório": random.sample(range(1, 1000), 20)
    }

    resultados = []
    for nome, lista in casos.items():
        resultados.append(["Merge Sort", nome, *execucaoM(lista).values()])

    headers = ["Algoritmo", "Caso", "Comparações", "Movimentos", "Tempo (s)", "Complexidade Teórica"]
    print("\n===== Tabela comparativa MergeSort =====\n")
    print(tabulate(resultados, headers=headers, floatfmt=".8f", tablefmt="grid"))


def analise_teorica(lista: List[int], showTabela: bool = False) -> Dict[str, object]:
    """
    Executa Merge Sort e, se showTabela=True,
    imprime a tabela de contagem e os cálculos de f(n).
    """
    global compporElemento, CopiasMG
    compporElemento = 0
    CopiasMG = 0
    inicio = time.perf_counter()
    ordenada = merge_count(lista)
    fim = time.perf_counter()

    resultado = {
        "ordenada": ordenada,
        "comparacoes": compporElemento,
        "copias": CopiasMG,
        "tempo_s": fim - inicio,
    }

    if showTabela:
        # ===== TABELA DE CONTAGEM =====
        headers = ["Instrução", "Médio", "Melhor", "Pior"]
        tabela = [
            ["if len(lista) <= 1", "2", "2", "2"],
            ["return lista[:]", "2", "2", "2"],
            ["meio = len(lista)//2", "3", "3", "3"],
            ["esquerda = merge_count(...)", "f(n/2)+2", "f(n/2)+2", "f(n/2)+2"],
            ["direita = merge_count(...)", "f(n/2)+2", "f(n/2)+2", "f(n/2)+2"],
            ["i = 0", "1", "1", "1"],
            ["j = 0", "1", "1", "1"],
            ["resultado = []", "1", "1", "1"],
            ["while i < len(esq) and j < len(dir)", "5(n+1)", "5(n+1)", "5(n+1)"],
            ["compporElemento += 1", "2n", "2n", "2n"],
            ["if esquerda[i] <= direita[j]", "3n", "3n", "3n"],
            ["resultado.append(...)", "2n", "2n", "2n"],
            ["CopiasMG += 1", "2n", "2n", "2n"],
            ["i += 1 / j += 1", "2n", "2n", "2n"],
            ["while i < len(esquerda)", "2(n/2+1)", "2(n/2+1)", "2(n/2+1)"],
            ["resultado.append(esq[i])", "2(n/2)", "2(n/2)", "2(n/2)"],
            ["CopiasMG += 1", "2(n/2)", "2(n/2)", "2(n/2)"],
            ["i += 1", "2(n/2)", "2(n/2)", "2(n/2)"],
            ["while j < len(direita)", "2(n/2+1)", "2(n/2+1)", "2(n/2+1)"],
            ["resultado.append(dir[j])", "2(n/2)", "2(n/2)", "2(n/2)"],
            ["CopiasMG += 1", "2(n/2)", "2(n/2)", "2(n/2)"],
            ["j += 1", "2(n/2)", "2(n/2)", "2(n/2)"],
            ["return resultado", "1", "1", "1"],
        ]
        print("\n===== Tabela de Contagem do Merge Sort =====\n")
        print(tabulate(tabela, headers=headers, tablefmt="grid"))

        # ===== CÁLCULOS DA FUNÇÃO f(n) =====
        print("\n===== Cálculo da Função de Complexidade f(n) =====\n")
        print("f(n) = 2 + 2 + 3 + f(n/2)+2 + f(n/2)+2 + 1 + 1 + 1 + 5(n+1) "
              "+ 2n + 3n + 2n + 2n + 2n + 2(n/2+1) + 2(n/2) + 2(n/2) "
              "+ 2(n/2) + 2(n/2+1) + 2(n/2) + 2(n/2) + 2(n/2) + 1")

        print("\nSimplificação → f(n) = 24 + 30n + 2f(n/2)")

        print("\nExpandindo a recorrência:")
        print("f(n) = 24 + 30n + 2f(n/2)")
        print("f(n/2) = 24 + 30(n/2) + 2f(n/4)")
        print("f(n/4) = 24 + 30(n/4) + 2f(n/8)")
        print("...")
        print("f(2) = 24 + 30*2 + 2f(1)")
        print("f(1) = 4")
        
        print("\nf(n) = 30n*log2n + 28n - 24 ∈ Θ(n log n)")

        print("\n✅ Conclusão: Todos os casos do Merge Sort têm a mesma complexidade,"
              " pois não dependem da ordem dos valores.")

    return resultado


# ================== TESTE LOCAL =====================
if __name__ == "__main__":
    comparacao()
    lista_ordenada = list(range(1, 21))
    lista_inversa = list(range(20, 0, -1))
    lista_aleatoria = random.sample(range(1, 100), 20)

    # Exemplo com tabela teórica
    print("\n===== Análise Teórica (com tabela) =====")
    analise_teorica(lista_aleatoria, showTabela=True)