from src.conta import Conta
from unittest.mock import Mock
from src.servico_email import ServicoEmail

def test_envio_email_ao_depositar():
    mock_email = Mock()
    conta = Conta(numero=123, titular="ragnar@email.com", saldo=100, notificador=mock_email)

    conta.depositar(50)

    mock_email.enviar_email.assert_called_once_with(
        destinatario="ragnar@email.com",
        assunto="Depósito recebido",
        corpo="Depósito de R$50.00 realizado com sucesso."
    )