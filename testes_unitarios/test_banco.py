from src.banco import Banco
from src.conta_corrente import ContaCorrente
from src.conta_poupanca import ContaPoupanca
import pytest

def test_criar_e_buscar_conta_corrente():
    banco = Banco("Meu Banco")
    cc = ContaCorrente(101, "Samuel", 100)
    banco.adicionar_conta(cc)
    conta_encontrada = banco.buscar_conta(101)
    assert conta_encontrada.ver_saldo() == 100

def test_criar_conta_com_numero_repetido():
    banco = Banco("Meu Banco")
    banco.adicionar_conta(ContaPoupanca(102, "Severino"))
    with pytest.raises(ValueError):
        banco.adicionar_conta(ContaPoupanca(102,"Severino"))

def test_transferencia_entre_contas():
    banco = Banco("Meu Banco")
    banco.adicionar_conta(ContaCorrente(201, "Jorge", 500))
    banco.adicionar_conta(ContaPoupanca(202, "Josefa", 100))

    banco.transferir(201,202, 200)
    
    assert banco.saldo(201) < 300 #conta corrente cobra tarifa
    assert banco.saldo(202) == 300

def test_transferencia_com_saldo_insuficiente():
    banco = Banco("Meu Banco")
    banco.adicionar_conta(ContaCorrente(301, "Robson", 100, limite_cheque_especial=0))
    banco.adicionar_conta(ContaPoupanca(302, "Ester", 100))
    with pytest.raises(ValueError):
        banco.transferir(301, 302, 150)

