# Algoritmos de Ordenação — Trabalho Prático

Implementação, instrumentação e comparação experimental de algoritmos de ordenação em Python, para a disciplina de Estrutura de Dados (4º período).

Cada algoritmo conta **comparações** e **movimentações** de elementos, além do **tempo** de execução, e o projeto compara os resultados medidos com a análise teórica de complexidade.

## Arquivo

Todo o trabalho fica em `TP_Algoritmos_de_Ordenacao.ipynb`: implementações, testes de corretude, análise teórica, experimentos (E1 a E6) com gráficos e tabelas, discussão e, na Parte H, o relatório (introdução, fundamentação teórica, metodologia, resultados, análise crítica e conclusões). O notebook está salvo com as saídas da execução completa.

## Algoritmos implementados

| Grupo | Algoritmo | Variantes |
|---|---|---|
| Quadráticos | Bubble Sort (com parada antecipada), Selection Sort, Insertion Sort | |
| $O(n\log n)$ | Shellsort | sequências de *gaps* de Shell, Knuth e Ciura |
| | Merge Sort | |
| | Quicksort (partição de Lomuto) | pivô: último, aleatório e mediana de três |
| Lineares | Counting Sort | |
| | Radix Sort (LSD) | base 256 (padrão) e base 10; o E6 compara também a base 65 536 |
| | Bucket Sort | entrada: reais em [0, 1) |

Nenhuma rotina de ordenação pronta (`sort`, `sorted`, `heapq`, `numpy.sort`) é usada nos algoritmos. O `sorted()` aparece apenas nos testes de corretude, para gerar o gabarito.

## Requisitos

- Python 3.10 ou superior
- `numpy`, `pandas` e `matplotlib`
- Jupyter (para abrir os notebooks) ou `papermill` (para executar pela linha de comando)

## Instalação

```bash
# criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# instalar dependências
pip install numpy pandas matplotlib jupyter papermill
```

## Como executar

Pelo Jupyter: abra `TP_Algoritmos_de_Ordenacao.ipynb` e use **Kernel → Restart & Run All**.

Pela linha de comando, gerando uma cópia executada do notebook e um log com o andamento:

```bash
papermill TP_Algoritmos_de_Ordenacao.ipynb TP_executado.ipynb --log-output 2>&1 | tee execucao.log
```

A variável `MODO` (Parte F) escolhe entre `"completo"` (faixas de *n* e 5 *seeds* do relatório, de 30 a 90 minutos) e `"rapido"` (faixas reduzidas, para depuração).

## Como o projeto funciona

Todos os algoritmos são funções com a assinatura `f(v, c)`: recebem a lista `v` e um objeto `Contador` e devolvem a lista ordenada em ordem não decrescente.

- O `Contador` guarda `comp` (comparações) e `trocas` (movimentações).
- As funções auxiliares `menor`, `menor_ou_igual`, `trocar` e `escrever` fazem a operação e incrementam o contador; todos os algoritmos as usam.
- O dicionário `ALGORITMOS` (Parte D) registra cada variante com seu grupo (`quadratico`, `nlogn` ou `linear`) e o domínio de entrada (`int` ou `float01`).
- A Parte D roda a bateria de testes (casos-limite comparados com `sorted()`) e três testes próprios: estabilidade, vetor já ordenado e casos de borda com vetores pequenos.
- `rodar_experimento` (Parte F) gera um vetor por (tipo, *n*, *seed*), entrega uma cópia a cada algoritmo, mede só a chamada do algoritmo com `time.perf_counter()` e o coletor de lixo desligado, e confere a saída com `esta_ordenado` fora da medição.

### O que é contado

- **Comparações:** comparações entre elementos da entrada. Comparações de índices não são contadas.
- **Trocas:** cada *swap* conta 1 e cada escrita de um elemento no vetor conta 1. Por isso, nos algoritmos que usam escritas (Insertion, Shellsort, Merge, Counting, Radix e Bucket), o valor de "trocas" significa "movimentações".
- **Não comparativos:** Counting e Radix não comparam elementos, então têm zero comparações. No Bucket Sort, as comparações vêm do Insertion Sort dentro dos baldes.

## Experimentos

Os experimentos (E1 a E6) variam o tamanho da entrada, o tipo (aleatória, ordenada, inversa, quase ordenada, muitos repetidos) e o domínio, com 5 *seeds* fixas (11, 22, 33, 44, 55) para garantir reprodutibilidade. Cada experimento salva seus resultados em `resultados_E1.csv` a `resultados_E6.csv`, com uma linha por execução (tempo, comparações e movimentações).

## Autores

- Arthur Silva Teixeira (2024021870)
- Rafael Campello Soares (2024017457)
