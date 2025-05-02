from src.conta_corrente import ContaCorrente
from src.conta_poupanca import ContaPoupanca
from src.conta import Conta


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self._contas = {}


    def adicionar_conta(self, conta):
        if conta._numero in self._contas:
            raise ValueError("Conta já existe")
        self._contas[conta._numero] = conta


    def buscar_conta(self, numero):
        if numero not in self._contas:
            raise ValueError("Conta não encontrada")
        return self._contas[numero]
    
    def transferir(self, numero_origem, numero_destino, valor):
        conta_origem = self.buscar_conta(numero_origem)
        conta_destino = self.buscar_conta(numero_destino)

        conta_origem.sacar(valor)
        conta_destino.depositar(valor)

    def saldo(self, numero):
        return self.buscar_conta(numero).ver_saldo()