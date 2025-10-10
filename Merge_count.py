import random
import time
from typing import List, Dict

# ====================== MERGE SORT ===========================
comparacoes_ms = 0
copias_ms = 0  # conta atribuições durante o merge (escritas na lista de saída)

def merge_count(lista: List[int]) -> List[int]:
    """
    Merge Sort recursivo com contadores globais.
    Atualiza comparacoes_ms (comparações entre elementos)
    e copias_ms (escritas durante o merge).
    """
    global comparacoes_ms, copias_ms
    if len(lista) <= 1:
        return lista[:]

    meio = len(lista) // 2
    esquerda = merge_count(lista[:meio])
    direita = merge_count(lista[meio:])

    i = j = 0
    resultado: List[int] = []

    # processo de intercalação (merge)
    while i < len(esquerda) and j < len(direita):
        comparacoes_ms += 1
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            copias_ms += 1
            i += 1
        else:
            resultado.append(direita[j])
            copias_ms += 1
            j += 1

    # adiciona o restante das listas
    while i < len(esquerda):
        resultado.append(esquerda[i])
        copias_ms += 1
        i += 1
    while j < len(direita):
        resultado.append(direita[j])
        copias_ms += 1
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
    global comparacoes_ms, copias_ms
    comparacoes_ms = 0
    copias_ms = 0
    inicio = time.perf_counter()
    merge_count(lista)
    fim = time.perf_counter()

    return {
        "comparacoes": comparacoes_ms,
        "movimentos": copias_ms,
        "tempo": fim - inicio,
        "complexidade": "O(n log n) em todos os casos"
    }


# ====================== TESTE LOCAL ===========================
if __name__ == "__main__":
    lista_ordenada = list(range(1, 201))
    lista_inversa = list(range(200, 0, -1))
    lista_aleatoria = random.sample(range(1, 10000), 200)

    for nome, lst in (
        ("ordenado", lista_ordenada),
        ("inverso", lista_inversa),
        ("aleatorio", lista_aleatoria),
    ):
        resultado = execucaoM(lst)
        print(f"\n#### Merge Sort — caso: {nome} ####")
        print(f"Comparações (merge): {resultado['comparacoes']}")
        print(f"Movimentos/copias: {resultado['movimentos']}")
        print(f"Tempo: {resultado['tempo']:.8f} s")
        print(f"Complexidade: {resultado['complexidade']}")
