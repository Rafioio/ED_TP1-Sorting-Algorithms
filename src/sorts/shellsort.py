from src.sort import Sort
from src.sorts.insertionsort import InsercaoMixin


class Shellsort(InsercaoMixin, Sort):
    SEQUENCIAS = ("shell", "knuth", "ciura")

    def __init__(self, sequencia="ciura"):
        if sequencia not in self.SEQUENCIAS:
            raise ValueError(f"Sequência inválida: {sequencia}")
        super().__init__(f"Shell-{sequencia}")
        self.sequencia = sequencia

    def _gaps(self, n):
        if self.sequencia == "shell":
            gaps, g = [], n // 2
            while g > 0:
                gaps.append(g)
                g //= 2
            return gaps

        if self.sequencia == "knuth":
            gaps = [1]
            while 3 * gaps[-1] + 1 < n // 3:
                gaps.append(3 * gaps[-1] + 1)
        else:  # ciura
            gaps = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
            while gaps[-1] * 2.25 < n:
                gaps.append(int(gaps[-1] * 2.25))

        return [g for g in reversed(gaps) if g < n]

    def sort(self, data):
        for gap in self._gaps(len(data)):
            self._insercao(data, gap)