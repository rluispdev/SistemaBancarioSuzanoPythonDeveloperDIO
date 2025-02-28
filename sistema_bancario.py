
menu = """
===================
[ d ] - Depositar
[ s ] - Sacar
[ e ] - Extrato
[ q ] - Sair
===================
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

welcome = """
WELCOME TO THE RLUISPDEV BANK.

> Qual operação deseja realizar?
"""

print(welcome)

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito efetuado com sucesso! Saldo: R$ {saldo:.2f}")
        else:
            print("Erro: O valor do depósito deve ser maior que zero!")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a sacar: "))

            if valor > 0:
                if valor <= limite and saldo >= valor:
                    saldo -= valor
                    extrato += f"Saque: R$ {valor:.2f}\n"
                    numero_saques += 1
                    print(f"Saque efetuado com sucesso! Saldo atual: R$ {saldo:.2f}")
                elif valor > limite:
                    print("Valor  de saque acima do limite permitido! Saque não efetuado.")
                else:
                    print("Você não tem saldo suficiente para realizar o saque!")
            else:
                print(" ⚠️e O valor do saque deve ser maior que zero!")
        else:
            print("Limite de saques atingido!")

    elif opcao == "e":
        print("\n========= EXTRATO =========")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================\n")

    elif opcao == "q":
        print("""
Obrigado por utilizar o RLUISPDEV BANK!
Volte sempre! ✌🏼
        """)
        break

    else:
        print("Opção inválida! Tente novamente.")