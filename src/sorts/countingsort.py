from src.sort import Sort


class CountingSort(Sort):
    def __init__(self):
        super().__init__("Counting")

    def sort(self, data):
        if len(data) < 2:
            return
        menor_v, maior_v = min(data), max(data)
        cont = [0] * (maior_v - menor_v + 1)
        for x in data:
            cont[x - menor_v] += 1

        k = 0
        for valor, c in enumerate(cont, start=menor_v):
            for _ in range(c):
                self.escrever(data, k, valor)
                k += 1