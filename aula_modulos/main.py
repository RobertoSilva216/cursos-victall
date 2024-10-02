import meu_modulo
from meu_pacote import modulo1, modulo2

nome = input("Digite seu nome: ")
print(meu_modulo.saudacao(nome))

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))

print(f"A soma é: {modulo1.soma(num1, num2)}")
print(f"A subtração é: {modulo2.subtrai(num1, num2)}")