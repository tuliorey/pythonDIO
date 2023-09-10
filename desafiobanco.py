menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0


while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite quanto deseja depositar: "))
        
        if valor_deposito > 0: 
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Seu depósito foi de R$ {valor_deposito:.2f}. Agora seu saldo é R$ {saldo:.2f}.")
        else:
            print("Opção incorreta. Você precisa informar um valor válido")
        
    elif opcao == "s":
        
            valor_saque = float(input("Digite quanto deseja sacar: "))
            
            if (numero_saques < LIMITE_SAQUES):
                
                if (valor_saque < 0):
                    print("Digite um valor válido")
                elif (valor_saque <= saldo and valor_saque < 500):
                    saldo -= valor_saque
                    print(f"Seu saldo é: R$ {saldo:.2f}.")
                    numero_saques += 1
                    extrato += f"Saque: R$ {valor_saque:.2f}\n"
                elif (valor_saque > saldo):
                    print("Você não tem saldo suficiente para sacar esse valor.")
            else:
                print("Você excedeu seu limite diário de saques")
                
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
