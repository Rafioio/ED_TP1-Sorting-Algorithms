from data.data import ALGORITMOS

class Teste:
    def __init__(self, experimento, algoritmo, n, seeds):
        self.experimento = experimento
        self.algoritmo = ALGORITMOS[algoritmo]
        self.n = n
        self.seeds = seeds

    testes = []