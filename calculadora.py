import os

# Funções básicas da calculadora
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

# Função para limpar o console
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal da calculadora
def calculadora():
    while True:
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora... Até a próxima!")
            break  # Sai do loop, encerrando o programa

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: valor inválido. Digite números válidos.")
            continue  # Volta ao início do loop para tentar novamente

        # Realiza a operação escolhida e exibe o resultado
        if escolha == '1':
            resultado = somar(num1, num2)
            operacao = '+'
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            operacao = '-'
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            operacao = '*'
        elif escolha == '4':
            resultado = dividir(num1, num2)
            operacao = '/'
        else:
            print("Escolha inválida!")
            continue  # Volta ao início do loop

        # Limpa o console e exibe o resultado
        limpar_console()
        print(f"Resultado de {num1} {operacao} {num2} = {resultado}\n")

# Executa a calculadora
calculadora()
