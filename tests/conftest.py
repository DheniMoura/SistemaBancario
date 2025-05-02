import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))



import pytest
from src.banco import Banco
from src.conta_corrente import ContaCorrente
from src.conta_poupanca import ContaPoupanca
from src.conta import Conta
from unittest.mock import Mock

@pytest.fixture
def sistema_bancario():
    banco = Banco("Banco de Teste")

    mock_email, mock_cambio = Mock(), Mock()
    mock_cambio.obter_taxa_dolar.return_value = 5.0

    cc = ContaCorrente(numero=1, titular="laguerta@email.teste", saldo=1000, notificador=mock_email)
    cp = ContaPoupanca(numero=2, titular="moriarty@email.teste", saldo=900)

    banco.adicionar_conta(cc)
    banco.adicionar_conta(cp)

    return {
        "banco": banco,
        "cc": cc,
        "cp": cp,
        "mock_email": mock_email,
        "mock_cambio": mock_cambio
    }