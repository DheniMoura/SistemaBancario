from src.conta import Conta
    

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite_cheque_especial=500, tarifa_saque=2.5, notificador=None):
        super().__init__(numero, titular, saldo) #o que faz o super?
        self._limite = limite_cheque_especial
        self._tarifa_saque = tarifa_saque
        self._notificador = notificador

    def sacar(self, valor):
        total = valor + self._tarifa_saque
        if total > (self._saldo + self._limite):
            raise ValueError("Saldo + limite insuficiente")
        self._debitar(total)

    def sacar_em_dolar(self, valor_dolar, servico_cambio):
        taxa = servico_cambio.obter_taxa_dolar()
        self.sacar(valor_dolar * taxa)