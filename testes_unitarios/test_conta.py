from src.conta import Conta
from src.conta_corrente import ContaCorrente
from src.conta_poupanca import ContaPoupanca
import pytest
from unittest.mock import Mock

#Testes de conta genéricos
def test_deposito_invalido():
    conta = Conta(132, "Maria")
    conta.depositar(100)
    assert conta.ver_saldo() == 100

def test_deposito_invalido():
    conta = Conta(132, "Maria")
    with pytest.raises(ValueError): #o que faz o with?
        conta.depositar(-50)

def test_saque_valido():
    conta = Conta(132, "Maria", saldo=200)
    conta.sacar(50)
    assert conta.ver_saldo() == 150

def test_saque_invalido():
    conta = Conta(132, "Maria", saldo=100)
    with pytest.raises(ValueError):
        conta.sacar(-50)


#Testes de conta corrente
def test_saque_conta_corrente_com_tarifa():
    cc = ContaCorrente(1, "João", saldo=100, limite_cheque_especial=0)
    cc.sacar(50) #saque de 50 + 2.5 de tarifa
    assert cc.ver_saldo() == 47.5

def test_saque_conta_corrente_limite():
    cc = ContaCorrente(1, "João", saldo=100)
    cc.sacar(590) # 500(limite) + 100(saldo) -> 590(saque) + 2.5(tarifa) 
    assert cc.ver_saldo() == -492.5

def test_saque_conta_corrente_excede_limite():
    cc = ContaCorrente(1, "João", saldo=100)
    with pytest.raises(ValueError):
        cc.sacar(600) #600 + 2.5(tarifa) > limite + saldo (500 + 100)

def test_saque_em_dolar_usando_mock():
    cc = ContaCorrente(1, "Carlos", saldo=1000)

    mock_servico = Mock()
    mock_servico.obter_taxa_dolar.return_value = 5.0 # U$1 = R$5

    cc.sacar_em_dolar(10, mock_servico) # deve sacar R$50 + R$2.5 de tarifa de saque

    assert cc.ver_saldo() == 947.5 # R$1.000 - R$52.5



#Testes Conta Poupança
def test_saque_conta_poupanca_ok():
    cp = ContaPoupanca(2, "Pedro", saldo=200)
    cp.sacar(50)
    assert cp.ver_saldo() == 150

def test_saque_conta_poupanca_insuficiente():
    cp = ContaPoupanca(2, "Pedro", saldo=200)
    with pytest.raises(ValueError):
        cp.sacar(250)

def test_aplicacao_juros_conta_poupanca():
    cp = ContaPoupanca(2, "Pedro", saldo=1000)
    cp.aplicar_juros(5) #5%
    assert cp.ver_saldo() == 1050.0


