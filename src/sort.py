from abc import ABC, abstractmethod
import time


class Sort(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.comparacoes = 0
        self.trocas = 0
        self.tempo = 0.0

    def ordenar(self, data):
        self.comparacoes = 0
        self.trocas = 0

        esperado = sorted(data)

        inicio = time.perf_counter()
        self.sort(data) 
        self.tempo = time.perf_counter() - inicio

        if data != esperado:
            raise AssertionError(
                f"{self.nome} não ordenou corretamente o vetor."
            )

        return len(data), self.tempo

    @abstractmethod
    def sort(self, data):
        """Ordena `data` in-place."""

    def menor(self, a, b):
        self.comparacoes += 1
        return a < b

    def menor_ou_igual(self, a, b):
        self.comparacoes += 1
        return a <= b

    def trocar(self, v, i, j):
        v[i], v[j] = v[j], v[i]
        self.trocas += 1

    def escrever(self, v, i, valor):
        v[i] = valor
        self.trocas += 1

    def __str__(self):
        return (
            f"{self.nome:<15} | comparações: {self.comparacoes:>8} | "
            f"trocas: {self.trocas:>8} | tempo: {self.tempo:.6f}s"
        )

    def __repr__(self):
        return (
            f"Sort(nome={self.nome!r}, comparacoes={self.comparacoes}, "
            f"trocas={self.trocas}, tempo={self.tempo})"
        )