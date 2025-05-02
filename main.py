from src.banco import Banco
from src.conta_corrente import ContaCorrente
from src.conta_poupanca import ContaPoupanca
from src.servico_email import ServicoEmail
from src.servico_cambio import ServicoCambio

def main():
    email = ServicoEmail()
    cambio = ServicoCambio()
    banco = Banco(email)

    #Criar contas iniciais
    cc = ContaCorrente(numero=1, titular="Cleosvaldo")
    cp = ContaPoupanca(numero=2, titular="Dolores")
    banco.adicionar_conta(cc)
    banco.adicionar_conta(cp)

    while True:
        print("\n--- SISTEMA BANCÁRIO ---")
        print("1. Ver saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Sacar em dólar")
        print("0. Sair")

        opcao = input("Escolha uma opção")

        if opcao == "0":
            break
        elif opcao in {"1", "2", "3", "4", "5"}:
            conta_id = int(input("ID da conta: "))
            conta = banco._contas.get(conta_id)

            if not conta:
                print("Conta não encontrada.")
                continue

            if opcao == "1":
                print(f"Saldo: R$ {conta._saldo}")
            elif opcao == "2":
                valor = float(input("Valor a depositar: "))
                conta.depositar(valor)
            elif opcao == "3":
                valor = float(input("Valor a sacar: "))
                conta.sacar(valor)
            elif opcao == "4":
                destino_id = int(input("ID da conta de destino: "))
                valor = float(input("Valor a transferir: "))
                banco.transferir(conta_id, destino_id, valor)
            elif opcao == "5":
                valor_dolar = float(input("Valor em dólar a sacar: "))
                if hasattr(conta, "sacar_em_dolar"):
                    conta.sacar_em_dolar(valor_dolar, cambio)
                else:
                    print("Esta conta não permite saque em dólar")
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    main()