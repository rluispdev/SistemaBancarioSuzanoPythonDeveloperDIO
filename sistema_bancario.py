import datetime

menu = """
===================
[ c ] - Criar Conta
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
numero_operacoes = 0
LIMITE_OPERACOES = 10
conta_criada = False
ultima_data = datetime.date.today()

welcome = """
WELCOME TO THE RLUISPDEV BANK.

> Para começar, crie sua conta!
"""

print(welcome)
nome_usuario = input("Digite seu nome: ")
conta_criada = True
print(f"Conta criada com sucesso! Bem-vindo, {nome_usuario}.")

while True:
    data_atual = datetime.date.today()
    if data_atual != ultima_data:
        numero_operacoes = 0
        numero_saques = 0
        ultima_data = data_atual
    
    if numero_operacoes >= LIMITE_OPERACOES:
        print("\n--------------------------------  ⚠️  Aviso ---------------------------------")
        print("Limite de operações por dia atingido!")
        while True:
            opcao = input("\n[ e ] - Ver Extrato\n[ q ] - Sair\nDigite sua opção: ").lower()
            if opcao == "e":
                print("\n========= EXTRATO =========")
                print(extrato if extrato else "Nenhuma movimentação realizada.")
                print(f"\nSaldo atual: R$ {saldo:.2f}")
                print("===========================\n")
            elif opcao == "q":
                print("""
Obrigado por utilizar o RLUISPDEV BANK!
Volte sempre! 
                """)
                exit()
            else:
                print("Opção inválida! Tente novamente.")
    
    opcao = input(menu).lower()

    if opcao == "c":
        print("Conta já foi criada!")
    
    elif opcao == "d":
        if numero_operacoes < LIMITE_OPERACOES:
            valor = float(input("Digite o valor a depositar: "))
            
            if valor > 0:
                saldo += valor
                data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                extrato += f"[{data_hora}] Depósito: R$ {valor:.2f}\n"
                numero_operacoes += 1
                print(f"Depósito efetuado com sucesso! Saldo: R$ {saldo:.2f}")
            else:
                print("Erro: O valor do depósito deve ser maior que zero!")
        else:
            print("⚠️ Limite de operações por dia atingido!")
    
    elif opcao == "s":
        if numero_operacoes < LIMITE_OPERACOES:
            if numero_saques < LIMITE_SAQUES:
                valor = float(input("Digite o valor a sacar: "))
                
                if valor > 0:
                    if valor <= limite and saldo >= valor:
                        saldo -= valor
                        data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        extrato += f"[{data_hora}] Saque: R$ {valor:.2f}\n"
                        numero_saques += 1
                        numero_operacoes += 1
                        print(f"Saque efetuado com sucesso! Saldo atual: R$ {saldo:.2f}")
                    elif valor > limite:
                        print("Valor de saque acima do limite permitido! Saque não efetuado.")
                    else:
                        print("Você não tem saldo suficiente para realizar o saque!")
                else:
                    print("⚠️ O valor do saque deve ser maior que zero!")
            else:
                print("⚠️ Limite de saques atingido!")
        else:
            print("⚠️ Limite de operações por dia atingido!")
    
    elif opcao == "e":
        print("\n========= EXTRATO =========")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("===========================\n")
    
    elif opcao == "q":
        print("""
Obrigado por utilizar o RLUISPDEV BANK!
Volte sempre!
        """)
        break
    
    else:
        print("Opção inválida! Tente novamente.")
