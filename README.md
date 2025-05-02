# Sistema Bancário Simples

## Conceitos praticados
Classe e objetos |	Conta, Cliente, Banco
Herança |	ContaCorrente e ContaPoupanca
Encapsulamento |	Saldo protegido, métodos públicos
Polimorfismo |	Métodos diferentes em contas distintas
Testes com pytest |	Testes unitários e teste de integração
Mock |	Mock do pytest para simular a consulta a uma API externa, cujo retorno é a cotação atual do dólar.


## Funcionalidades do Banco
- Cadastrar contas (corrente e poupança).
- Buscar contas por número.
- Realizar operações (depósito, saque, transferência).
- Ver saldo de uma conta.


# e-mail
- Sempre que uma conta fizer um depósito, um e-mail de notificação será enviado.
- Usamos um serviço externo de email (classe ServicoEmail).
- Nos testes, usamos o mock para verificar se o e-mail foi enviado corretamente.


# MELHORIAS
- Persistir os dados, com arquivos ou SQLite, por exemplo
- Autenticação com senha
- Interface gráfica com TKinter ou web com flask



# RODANDO OS TESTES

Primeiro é necessário iniciar o ambiente virtual utilisando o seguinte código

Caso precise criar o ambiente virtual:
python -m venv .venv 

Iniciando o ambiete virtual:
.venv\Scripts\Activate.ps1  # (ou source .venv/bin/activate no Linux/macOS)

Instalando o pytest
pip install pytest pytest-cov


## Testes de integração

pytest --cov=src tests/


## Testes unitários

pytest --cov=src testes_unitarios/


## Testes de integração + Testes unitários

pytest


# RODANDO A APLICAÇÃO

Abrir um terminal na pasta raiz e executar o seguinte comando:

python main.py
