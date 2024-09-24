def imprime():
    print("esta é uma função")

imprime()

#com parametro
def imprime(n):
    print(n)

imprime("Impressão deste texto")


#com retorno
def potencia(n):
    return n * n

x = potencia(3)

#com valor default
def intervalo(inic=1,fim=10):
    for inic in range(1, fim+1):
        print(inic)

intervalo(1,10)
intervalo()
