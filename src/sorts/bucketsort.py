from src.sort import Sort
from src.sorts.insertionsort import InsercaoMixin


class BucketSort(InsercaoMixin, Sort):
    """Espera floats em [0, 1)."""

    def __init__(self):
        super().__init__("Bucketsort")

    def sort(self, data):
        n = len(data)
        if n < 2:
            return
        baldes = [[] for _ in range(n)]
        for x in data:
            baldes[min(int(x * n), n - 1)].append(x)

        k = 0
        for b in baldes:
            self._insercao(b, 1)
            for x in b:
                self.escrever(data, k, x)
                k += 1