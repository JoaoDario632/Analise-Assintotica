# 🔢 Análise de Algoritmos de Ordenação com Contadores de Operações

Este projeto implementa e analisa três algoritmos clássicos de ordenação — **Insertion Sort**, **Merge Sort** e **Quick Sort** — com **contadores explícitos** de operações fundamentais (comparações, movimentações e cópias).  
O objetivo é comparar o desempenho prático e teórico de cada método, evidenciando seu comportamento em diferentes cenários de entrada.

---

## 📚 Estrutura do Projeto

```
├── Insertion_count.py
├── Merge_count.py
├── Quick_count.py
├── Readme.md
└── LICENSE
```

Cada arquivo contém:
- A implementação do algoritmo.
- Contadores de operações (comparações, deslocamentos, cópias ou movimentos).
- Execução com três tipos de entrada: ordenada, inversa e aleatória.
- Relatório no console com estatísticas de execução.

---

## ⚙️ Tecnologias Utilizadas

- **Linguagem:** Python 3.8+
- **Bibliotecas:** `time`, `random`, `typing`
- **Execução:** CLI (linha de comando)

---

## 🧩 Descrição dos Algoritmos

### 🟦 Insertion Sort — `Insertion_count.py`
**Ideia:** percorre o vetor inserindo cada elemento em sua posição correta em relação aos anteriores.  
**Complexidade:**
| Caso | Comparações / Deslocamentos | Complexidade |
|------|-----------------------------|---------------|
| Melhor (ordenado) | ~n | O(n) |
| Médio | ~n²/4 | O(n²) |
| Pior (inverso) | ~n²/2 | O(n²) |

**Contadores:**
- `comparacoes`: número de comparações `arr[j] > chave`
- `deslocamentos`: número de movimentações dentro do vetor

---

### 🟩 Merge Sort — `Merge_count.py`
**Ideia:** algoritmo recursivo de **divisão e conquista**. Divide o vetor ao meio, ordena as partes e as intercala.  
**Complexidade:**
| Caso | Comparações / Cópias | Complexidade |
|------|----------------------|---------------|
| Melhor | ~n log n | O(n log n) |
| Médio | ~n log n | O(n log n) |
| Pior | ~n log n | O(n log n) |

**Contadores:**
- `comparacoes`: número de comparações durante a mesclagem
- `copias`: número de escritas no vetor resultante

---

### 🟥 Quick Sort — `Quick_count.py`
**Ideia:** seleciona um **pivô** e particiona o vetor em três partes: menores, iguais e maiores.  
**Complexidade:**
| Caso | Comparações / Movimentos | Complexidade |
|------|--------------------------|---------------|
| Melhor | ~n log n | O(n log n) |
| Médio | ~1,39 n log n | O(n log n) |
| Pior (ordenado) | ~n² | O(n²) |

**Contadores:**
- `comparacoes`: número de comparações com o pivô
- `movimentos`: número de inserções e concatenações

---

## 📊 Exemplos de Saída (resumo)

```
#### Insertion Sort — caso: aleatorio ####
Comparações: 88
Deslocamentos: 67
Tempo: 0.00032145 s

#### Merge Sort — caso: inverso ####
Comparações: 526
Escritas/copias: 597
Tempo: 0.00145268 s

#### Quick Sort — caso: ordenado ####
Comparações: 398
Movimentos: 600
Tempo: 0.00109321 s
```

---

## ▶️ Como Executar

### 1. Clone o repositório ou baixe os arquivos:
```bash
git clone https://github.com/seuusuario/analise-algoritmos.git
cd analise-algoritmos
```

### 2. Execute o script desejado:
```bash
python Insertion_count.py
python Merge_count.py
python Quick_count.py
```

### 3. (Opcional) Execute no VS Code:
- Abra a pasta do projeto no VS Code.
- Clique com o botão direito no arquivo Python e selecione **"Run Python File in Terminal"**.
- Veja as estatísticas impressas no terminal.

---

## 📈 Considerações Analíticas

| Algoritmo | Vantagens | Desvantagens |
|------------|------------|---------------|
| **Insertion Sort** | Simples, eficiente para listas pequenas ou quase ordenadas. | Ineficiente para grandes volumes (O(n²)). |
| **Merge Sort** | Estável e com desempenho previsível. | Consome memória adicional para sublistas. |
| **Quick Sort** | Muito rápido em média, bom uso de cache. | Pode atingir O(n²) em piores casos se o pivô for mal escolhido. |

---

## 🧠 Conclusão

Este estudo evidencia como a **complexidade teórica** se reflete em **operações práticas** (comparações e movimentações).  
Cada algoritmo possui vantagens específicas que o tornam mais apropriado para determinados tipos de dados e contextos de uso.

---

## 👨‍💻 Autores
<table>
  <tr>
     <td align="center">
       <a href="https://github.com/Otto-Samuel">
         <img src="https://avatars.githubusercontent.com/u/162514493?v=4" style="border-radius: 50%" width="100px;" alt="Otto Samuel"/>
         <br />
         <sub><b>Otto Samuel 💻👑</b></sub>
       </a>
     </td>
    <td align="center">
       <a href="https://github.com/LucasAugustoSS">
         <img src="https://avatars.githubusercontent.com/u/126918429?v=4" style="border-radius: 50%" width="100px;" alt="Lucas augusto"/>
         <br />
         <sub><b>Lucas Augusto 💻👑</b></sub>
       </a>
     </td>
    <td align="center">
       <a href="https://github.com/FrrTiago">
         <img src="https://avatars.githubusercontent.com/u/132114628?v=4" style="border-radius: 50%" width="100px;" alt="ferreira"/>
         <br />
         <sub><b>Tiago Ferreira 💻👑</b></sub>
       </a>
     </td>
     <td align="center">
       <a href="https://github.com/JoaoDario632">
         <img src="https://avatars.githubusercontent.com/u/134674876?v=4" style="border-radius: 50%" width="100px;" alt="ferreira"/>
         <br />
         <sub><b>João Dário 💻👑</b></sub>
       </a>
     </td>
  </tr>
</table>

📅 Projeto desenvolvido para fins acadêmicos — Análise de Algoritmos  
🧮 Universidade / Curso: [CESUPA - ANÁLISE E PROJETO DE ALGORITMOS]