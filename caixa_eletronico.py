import os
def limpar_console():
    # Verifica o sistema operacional e limpa o console
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux e MacOS
        os.system('clear')


saldo = 1000  # Saldo inicial da conta

# Função para verificar o saldo
def verificar_saldo(saldo):
    limpar_console()
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")

# Função para realizar o saque
def realizar_saque(saldo):
    valor_saque = float(input("\nDigite o valor que deseja sacar: R$ "))
    limpar_console()
    if valor_saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor_saque <= 0:
        print("Valor de saque inválido. Tente novamente.")
    else:
        saldo -= valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    
    return saldo

def depositar():
    global saldo
    valor = float(input("Qual valor deseja depositar?"))
    saldo +=valor
    limpar_console()
    print(f"Foi depositado o valor de R$ {valor:.2f}")
    print(f"Seu saldo atual é: R$ {saldo:.2f}")



print("Bem-vindo ao Caixa Eletrônico!")
while True:
    print("\nSelecione uma opção:")
    print("1. Verificar saldo")
    print("2. Sacar dinheiro")
    print("3. Depositar")
    print("4. Sair")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        verificar_saldo(saldo)
    elif opcao == "2":
        saldo = realizar_saque(saldo)
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        print("Obrigado por usar o Caixa Eletrônico. Tenha um bom dia!")
        break
    else:
        print("Opção inválida. Tente novamente.")

    



