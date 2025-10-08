import time
import random
from typing import List, Dict

def insertion_count(lista: List[int]) -> Dict[str, object]:
    """
    Insertion Sort com contadores de operações.
    Retorna dicionário com lista ordenada, comparações, deslocamentos e tempo em segundos.
    """
    comparacoes = 0       # conta comparações entre elementos (lista[j] > chave)
    deslocamentos = 0     # conta deslocamentos (atribuições que movem elementos para a direita)
    n = len(lista)
    arr = lista[:]        # trabalhar em cópia para não modificar entrada
    inicio = time.perf_counter()

    for i in range(1, n):                # executa n-1 vezes
        chave = arr[i]
        j = i - 1
        # cada iteração do while pode executar até i vezes
        while j >= 0 and arr[j] > chave:
            comparacoes += 1            # comparação lista[j] > chave (quando verdadeira)
            arr[j + 1] = arr[j]
            deslocamentos += 1
            j -= 1
        # se o while terminou por arr[j] <= chave, contamos essa última comparação (quando j >= 0)
        if j >= 0:
            comparacoes += 1
        arr[j + 1] = chave

    fim = time.perf_counter()
    return {
        'ordenada': arr,
        'comparacoes': comparacoes,
        'deslocamentos': deslocamentos,
        'tempo_s': fim - inicio
    }

if __name__ == "__main__":
    # Exemplos: ordenado, inverso, aleatório (tamanhos pequenos para demonstração)
    bases = {
        'ordenado': list(range(1, 21)),
        'inverso': list(range(20, 0, -1)),
        'aleatorio': random.sample(range(1, 1000), 20)
    }

    for nome, lista in bases.items():
        resultado = insertion_count(lista) # Imprime o resultado do Insertion Sort
        print(f"\n#### Insertion Sort — caso: {nome} ####")
        print(f"Comparações: {resultado['comparacoes']}")
        print(f"Deslocamentos: {resultado['deslocamentos']}")
        print(f"Tempo: {resultado['tempo_s']:.8f} s")