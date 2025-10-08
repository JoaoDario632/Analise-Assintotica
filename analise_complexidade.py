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