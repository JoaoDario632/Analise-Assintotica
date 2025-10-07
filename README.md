# 🧮 Análise de Complexidade de Algoritmos

## QuickSort • InsertionSort • MergeSort

### 📘 Descrição

Este projeto tem como objetivo analisar e comparar o desempenho de três algoritmos clássicos de ordenação:

* **QuickSort**
* **InsertionSort**
* **MergeSort**

### 🧱 Estrutura do Projeto
```
📂 AnaliseAlgoritmos/
 ├── insertion_sort.py
 ├── quick_sort.py
 ├── merge_sort.py
 ├── README.md
```
---
### ⚙️ Execução dos Algoritmos

Todos os algoritmos podem ser executados individualmente com Python 3:

```
Insertion.py
Quick.py
Merge.py
```

Cada script exibe:

* A lista ordenada,
* O número de **comparações** e **trocas** realizadas,
* O **tempo de execução (em segundos)**.

---

### 📊 Análise Teórica

| Algoritmo         | Melhor Caso | Pior Caso  | Caso Médio | Complexidade Assintótica                |
| ----------------- | ----------- | ---------- | ---------- | --------------------------------------- |
| **InsertionSort** | Ω(n)        | O(n²)      | Θ(n²)      | Simples, eficiente para listas pequenas |
| **QuickSort**     | Ω(n log n)  | O(n²)      | Θ(n log n) | Geralmente o mais rápido                |
| **MergeSort**     | Ω(n log n)  | O(n log n) | Θ(n log n) | Estável e previsível                    |

---

### 🧠 Conclusão

Os resultados obtidos confirmam que:

* **InsertionSort** é eficiente apenas para listas pequenas ou quase ordenadas.
* **QuickSort** apresenta o melhor desempenho médio, mas pode degradar no pior caso.
* **MergeSort** mantém desempenho estável e eficiente, mesmo em grandes conjuntos de dados.

Assim, o **MergeSort** e o **QuickSort** são os algoritmos mais indicados para aplicações práticas que envolvem grandes volumes de dados.

---

### 🧾 Referências

* Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. *Introduction to Algorithms*. MIT Press.
* Sedgewick, R., & Wayne, K. *Algorithms, 4th Edition*. Addison-Wesley.
