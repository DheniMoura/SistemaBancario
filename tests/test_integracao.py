
import pytest

def test_fluxo_completo(sistema_bancario):
    banco = sistema_bancario["banco"]
    cc = sistema_bancario["cc"]
    cp = sistema_bancario["cp"]
    mock_email = sistema_bancario["mock_email"]
    mock_cambio = sistema_bancario["mock_cambio"]

    #depósito
    cc.depositar(100)
    mock_email.enviar_email.assert_called_once()

    # Transferência
    banco.transferir(1, 2, 200)
    assert banco.saldo(1) == pytest.approx(897.5)
    assert banco.saldo(2) == 1100

    # Saque em dólar
    cc.sacar_em_dolar(10, servico_cambio=mock_cambio)
    assert banco.saldo(1) == pytest.approx(845)

    # Limite saque poupança
    cp.sacar(100)
    cp.sacar(100)
    cp.sacar(100)
    with pytest.raises(ValueError):
        cp.sacar(100)
