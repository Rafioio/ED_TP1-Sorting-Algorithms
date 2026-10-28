from src.sort import Sort


class Selectionsort(Sort):
    def __init__(self):
        super().__init__("Selectionsort")

    def sort(self, data):
        n = len(data)
        for i in range(n - 1):
            m = i
            for j in range(i + 1, n):
                if self.menor(data[j], data[m]):
                    m = j
            if m != i:
                self.trocar(data, i, m)