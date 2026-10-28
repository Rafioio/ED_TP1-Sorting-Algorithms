import random
from data.data import ALGORITMOS

def gerar(dominio, n):
    if dominio == "float01":
        return [random.random() for _ in range(n)]
    return [random.randint(0, 10_000) for _ in range(n)]

for nome, cfg in ALGORITMOS.items():
    alg = cfg["fabrica"]()                 # instância nova = contadores zerados
    dados = gerar(cfg["dominio"], 1000)
    alg.ordenar(dados)
    print(alg)