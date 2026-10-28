from src.sort import Sort


class RadixSort(Sort):
    def __init__(self, base=256):
        super().__init__(f"Radix-{base}")
        self.base = base

    def sort(self, data):
        n = len(data)
        if n < 2:
            return
        minimo = min(data)                 # deslocamento p/ aceitar negativos
        amplitude = max(data) - minimo
        exp = 1
        while amplitude // exp > 0:
            self._passada(data, exp, minimo)
            exp *= self.base

    def _passada(self, v, exp, minimo):
        n, base = len(v), self.base
        cont = [0] * base
        for x in v:
            cont[((x - minimo) // exp) % base] += 1
        for i in range(1, base):
            cont[i] += cont[i - 1]

        saida = [0] * n
        for i in range(n - 1, -1, -1):     # de trás pra frente: estável
            d = ((v[i] - minimo) // exp) % base
            cont[d] -= 1
            saida[cont[d]] = v[i]

        for i in range(n):
            self.escrever(v, i, saida[i])