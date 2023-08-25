menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_DIARIO_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "1":
        valor_depositado = float(input("Informe o valor do depósito: "))

        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Déposito: R$ {valor_depositado:.2f}\n"

        else:
            print("Falha na operação! O valor informado é inválido.")

    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numeros_saques >= LIMITE_DIARIO_SAQUES
        
        if excedeu_saldo:
            print("Falha na operação! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Falha na operação! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Falha na operação! Número máximo de saques excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numeros_saques += 1
            
        else:
            print("Falha na operação! O valor informado é inválido.")
        

    elif opcao == "3":
        print("\n===================== Extrato =====================")
        print("Não foram realizado movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")