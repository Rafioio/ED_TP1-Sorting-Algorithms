from src.sort import Sort

class Bubblesort(Sort):
    def __init__(self):
        super().__init__("Bubblesort")

    def sort(self, data):
        n = len(data)
        for i in range(n):
            trocou = False
            for j in range(n - i - 1):
                if self.menor(data[j + 1], data[j]):
                    self.trocar(data, j, j + 1)
                    trocou = True
            if not trocou:
                break