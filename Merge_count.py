import time
import random
from typing import List, Tuple

# contadores globais (zerar antes de cada experimento)
comparacoes_ms = 0
copias_ms = 0  # conta atribuições durante merge (escritas em saída)


def merge_count(lista: List[int]) -> List[int]:
    """
    Merge Sort com contadores globais.
    Retorna lista ordenada. Os contadores são atualizados nas variáveis globais.
    """
    global comparacoes_ms, copias_ms
    if len(lista) <= 1:
        return lista[:]

    meio = len(lista) // 2
    esquerda = merge_count(lista[:meio])
    direita = merge_count(lista[meio:])

    i = j = 0
    resultado: List[int] = []
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

    # copiar o restante
    while i < len(esquerda):
        resultado.append(esquerda[i])
        copias_ms += 1
        i += 1
    while j < len(direita):
        resultado.append(direita[j])
        copias_ms += 1
        j += 1

    return resultado


def run_and_report(lista):
    global comparacoes_ms, copias_ms
    comparacoes_ms = 0
    copias_ms = 0
    inicio = time.perf_counter()
    ordenada = merge_count(lista)
    fim = time.perf_counter()
    return {
        "ordenada": ordenada,
        "comparacoes": comparacoes_ms,
        "copias": copias_ms,
        "tempo_s": fim - inicio,
    }


if __name__ == "__main__":
    # Exemplos: ordenado, inverso, aleatório
    lista_ordenada = list(range(1, 201))
    lista_inversa = list(range(200, 0, -1))
    lista_aleatoria = random.sample(range(1, 10000), 200)

    for nome, lst in (
        ("ordenado", lista_ordenada),
        ("inverso", lista_inversa),
        ("aleatorio", lista_aleatoria),
    ):
        resultado = run_and_report(lst)
        print(f"\n#### Merge Sort — caso: {nome} ####")
        print(f"Comparações (merge): {resultado['comparacoes']}")
        print(f"Escritas/copias (merge): {resultado['copias']}")
        print(f"Tempo: {resultado['tempo_s']:.8f} s")
