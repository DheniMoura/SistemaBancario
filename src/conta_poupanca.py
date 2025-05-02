from src.conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo=0, limite_saque=3):
        super().__init__(numero, titular, saldo)
        self._limite_saque = limite_saque
        self._saques_realizados = 0

    def sacar(self, valor):
        if self._saques_realizados >= self._limite_saque or valor > self._saldo:
            raise ValueError("saldo insuficiente ou limite de saques atingido")
        super().sacar(valor)
        self._saques_realizados += 1

    def aplicar_juros(self, taxa_percentual):
        if taxa_percentual < 0:
            raise ValueError("Taxa deve ser positiva")
        self._saldo *= (1 + taxa_percentual / 100)
