# Algoritmos de Ordenação — Trabalho Prático

Implementação, instrumentação e comparação experimental de algoritmos de ordenação em Python, para a disciplina de Estrutura de Dados (4º período).

Cada algoritmo conta **comparações** e **movimentações** de elementos, além do **tempo** de execução, e o projeto compara os resultados medidos com a análise teórica de complexidade.

## Algoritmos implementados

| Grupo | Algoritmo | Variantes |
|---|---|---|
| Quadráticos | Bubble Sort (com parada antecipada), Selection Sort, Insertion Sort | |
| $O(n\log n)$ | Shellsort | sequências de *gaps* de Shell, Knuth e Ciura |
| | Merge Sort | |
| | Quicksort (partição de Lomuto) | pivô: último, aleatório e mediana de três |
| Lineares | Counting Sort | |
| | Radix Sort (LSD) | base 256 (padrão) e base 10 |
| | Bucket Sort | entrada: reais em [0, 1) |

Nenhuma rotina de ordenação pronta (`sort`, `sorted`, `heapq`, `numpy.sort`) é usada nos algoritmos. O `sorted()` aparece apenas na verificação de corretude.

## Requisitos

- Python 3.10 ou superior
- Para os gráficos e tabelas do relatório: `numpy`, `pandas` e `matplotlib`

## Instalação

```bash
# criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt
```

## Como o projeto funciona

Todos os algoritmos herdam da classe base `Sort` (`src/sort.py`), que:

- zera os contadores a cada execução;
- mede o tempo com `time.perf_counter()`, apenas em torno da chamada do algoritmo;
- confere o resultado contra `sorted()` (fora da janela de medição) e lança erro se a saída estiver incorreta;
- oferece as operações contadas `menor`, `menor_ou_igual`, `trocar` e `escrever`, usadas por todos os algoritmos.

Cada subclasse implementa apenas o método `sort(data)`, que ordena o vetor **in-place**.

Para cada variante (gaps do Shellsort, pivô do Quicksort, base do Radix), o dicionário `ALGORITMOS` em `data/data.py` guarda uma fábrica que cria uma instância nova, com contadores zerados, e o domínio de entrada esperado (`int` ou `float01`).

### O que é contado

- **Comparações:** comparações entre elementos da entrada. Comparações de índices não são contadas.
- **Trocas:** cada *swap* conta 1 e cada escrita de um elemento no vetor conta 1. Por isso, nos algoritmos que usam escritas (Insertion, Shellsort, Merge, Counting, Radix e Bucket), o valor de "trocas" significa "movimentações".
- **Não comparativos:** Counting e Radix não comparam elementos, então têm zero comparações.

## Experimentos

Os experimentos (E1 a E6) variam o tamanho da entrada, o tipo (aleatória, ordenada, inversa, quase ordenada, muitos repetidos) e o domínio, com 5 *seeds* fixas (11, 22, 33, 44, 55) para garantir reprodutibilidade. Os resultados são salvos em CSV, e as tabelas e os gráficos estão no relatório (notebook).

## Relatório

O relatório completo, com a fundamentação teórica, a metodologia, os resultados e a análise, está em **TP_Algoritimos_de_Ordenacao.ipynb**. Para reproduzi-lo, abra o notebook e use **Kernel → Restart & Run All**.

## Autores

- Arthur Silva Teixeira (2024021870)
- Rafael Campello Soares (2024017457)