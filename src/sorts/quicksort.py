import random
from src.sort import Sort


class Quicksort(Sort):
    PIVOS = ("aleatorio", "mediana3", "ultimo")

    def __init__(self, pivo="ultimo"):
        if pivo not in self.PIVOS:
            raise ValueError(f"Pivô inválido: {pivo}")
        super().__init__(f"Quick-{pivo}")
        self.pivo = pivo

    def _escolher_pivo(self, v, lo, hi):
        """Move o pivô escolhido para a posição hi."""
        if self.pivo == "aleatorio":
            k = random.randint(lo, hi)
        elif self.pivo == "mediana3":
            a, b, c = lo, (lo + hi) // 2, hi
            if self.menor(v[a], v[b]):
                if self.menor(v[b], v[c]):
                    k = b
                elif self.menor(v[a], v[c]):
                    k = c
                else:
                    k = a
            else:
                if self.menor(v[a], v[c]):
                    k = a
                elif self.menor(v[b], v[c]):
                    k = c
                else:
                    k = b
        else:
            k = hi

        if k != hi:
            self.trocar(v, k, hi)

    def _particionar(self, v, lo, hi):
        self._escolher_pivo(v, lo, hi)
        pivo = v[hi]
        i = lo
        for j in range(lo, hi):
            if self.menor(v[j], pivo):
                if i != j:
                    self.trocar(v, i, j)
                i += 1
        if i != hi:
            self.trocar(v, i, hi)
        return i

    def sort(self, data):
        pilha = [(0, len(data) - 1)]
        while pilha:
            lo, hi = pilha.pop()
            if lo >= hi:
                continue
            p = self._particionar(data, lo, hi)
            # empilha o lado maior primeiro: a pilha fica O(log n)
            if (p - lo) > (hi - p):
                pilha.append((lo, p - 1))
                pilha.append((p + 1, hi))
            else:
                pilha.append((p + 1, hi))
                pilha.append((lo, p - 1))