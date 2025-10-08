import time
import random
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple

def gerar_relatorio():

    tamanhos = [10, 50, 100, 200, 500]
    resultados = {
        'insertion': {'ordenado': [], 'inverso': [], 'aleatorio': []},
        'merge': {'ordenado': [], 'inverso': [], 'aleatorio': []},
        'quick': {'ordenado': [], 'inverso': [], 'aleatorio': []}
    }

    print("=" * 80)
    print("RELATÓRIO DE ANÁLISE ASSINTÓTICA - ALGORITMOS DE ORDENAÇÃO")
    print("=" * 80)

    for n in tamanhos:
        print(f"\n📊 TESTE COM n = {n} elementos:")
        print("-" * 50)
        
        # Gerar dados de teste
        ordenado = list(range(1, n+1))
        inverso = list(range(n, 0, -1))
        aleatorio = random.sample(range(1, n*10), n)
        
        casos = {'ordenado': ordenado, 'inverso': inverso, 'aleatorio': aleatorio}

        for caso, dados in casos.items():
            print(f"\n🔹 Caso: {caso.upper()}")
            
            # Teste Insertion Sort
            from Insertion_count import insertion_count
            result_ins = insertion_count(dados)
            resultados['insertion'][caso].append({
                'n': n,
                'comparacoes': result_ins['comparacoes'],
                'operacoes': result_ins['deslocamentos'],
                'tempo': result_ins['tempo_s']
            })
            print(f"   Insertion: {result_ins['comparacoes']} comp, {result_ins['deslocamentos']} desl")

            # Teste Merge Sort  
            from Merge_count import run_and_report
            result_merge = run_and_report(dados)
            resultados['merge'][caso].append({
                'n': n,
                'comparacoes': result_merge['comparacoes'],
                'operacoes': result_merge['copias'],
                'tempo': result_merge['tempo_s']
            })
            print(f"   Merge:     {result_merge['comparacoes']} comp, {result_merge['copias']} copias")

            # Teste Quick Sort
            from Quick_count import run_and_report as quick_report
            result_quick = quick_report(dados)
            resultados['quick'][caso].append({
                'n': n,
                'comparacoes': result_quick['comparacoes'],
                'operacoes': result_quick['movimentos'],
                'tempo': result_quick['tempo_s']
            })
            print(f"   Quick:     {result_quick['comparacoes']} comp, {result_quick['movimentos']} mov")
            
    
    return resultados

if __name__ == "__main__":
    print(__doc__)
    gerar_relatorio()