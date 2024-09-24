#funções internas
print(abs(-200))
lst = [1,2,30,30,45]
print("Maior valor: ", max(lst))
print("Menor valor: ", min(lst))
print("Soma: ", sum(lst))
print("Arredondamento: ", round(2.34567,2))


#statistica
from statistics import *
print("Média: ", mean(lst))
print("Mediana: ", median(lst))
print("Moda: ", mode(lst))
#desvio padrão da amostra
print("Desvio padrão: ", stdev(lst))
#variancia da amostra
print("Variância: ", variance(lst))

from numpy import *
a = random.random((8,8))
print(type(a))
print(a)
