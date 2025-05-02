
class Conta:
    
    def __init__(self, numero, titular, saldo=0, notificador=None):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo  #por que tem _?
        self._notificador = notificador

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo") #o que faz o raise e o ValueError?
        self._saldo += valor

        if self._notificador:
            self._notificador.enviar_email(
                destinatario=self._titular,
                assunto="Depósito recebido",
                corpo=f"Depósito de R${valor:.2f} realizado com sucesso."
            )

    def sacar(self, valor):
        if not self._tem_saldo(valor):
            raise ValueError("Saldo insuficiente")
        elif valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self._saldo -= valor

    def ver_saldo(self):
        return self._saldo
    
    def _tem_saldo(self, valor):
        return self._saldo >= valor
    
    def _debitar(self, valor):
        self._saldo -= valor
