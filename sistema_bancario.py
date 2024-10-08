menu = """

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=> """

saldo = 0
LIMITE_SAQUE = 3
limite = 800
extrato = ""
numero_saque = 0

while True:
    opcao = input(menu)

    if opcao == "d": 
        valor = float(input("Informe um valor para depositar: "))

        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: valor informado inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite         
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Saldo insuficiente!')

        elif excedeu_limite:
            print('O valor do saque excede o limite.')

        elif excedeu_saque:
            print("Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou: valor inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
