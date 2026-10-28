from src.sort import Sort


class MergeSort(Sort):
    def __init__(self):
        super().__init__("Mergesort")

    def sort(self, data):
        n = len(data)
        if n < 2:
            return
        aux = [None] * n
        self._ordenar(data, aux, 0, n - 1)

    def _ordenar(self, v, aux, lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        self._ordenar(v, aux, lo, mid)
        self._ordenar(v, aux, mid + 1, hi)
        self._intercalar(v, aux, lo, mid, hi)

    def _intercalar(self, v, aux, lo, mid, hi):
        aux[lo:hi + 1] = v[lo:hi + 1]
        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                self.escrever(v, k, aux[j]); j += 1
            elif j > hi:
                self.escrever(v, k, aux[i]); i += 1
            elif self.menor(aux[j], aux[i]):   # estrito: mantém estabilidade
                self.escrever(v, k, aux[j]); j += 1
            else:
                self.escrever(v, k, aux[i]); i += 1