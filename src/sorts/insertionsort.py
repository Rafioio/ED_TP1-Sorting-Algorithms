from src.sort import Sort


class InsercaoMixin:
    """Inserção com salto `gap` (gap=1 é o insertion sort clássico)."""

    def _insercao(self, v, gap=1):
        for i in range(gap, len(v)):
            chave = v[i]
            j = i
            while j >= gap and self.menor(chave, v[j - gap]):
                self.escrever(v, j, v[j - gap])
                j -= gap
            if j != i:
                self.escrever(v, j, chave)


class Insertionsort(InsercaoMixin, Sort):
    def __init__(self):
        super().__init__("Insertionsort")

    def sort(self, data):
        self._insercao(data, 1)