#exemplo com while
count = 1
while count <= 5:
    print(count)
    count += 1


#range(0, 10, 1):
#range(inicio, parada, incremento)
#não inclui o valor de incremento (para isso usamos + 1 ou -1)
#O incremento pode ser negativo

#for normal
for n in range(0, 10):
    print(n)

#for decrecente
for n in range(10, 0,-1):
    print(n)

#exemplo com break
#vai parar no 3 pois o break está antes do print
for n in range(0, 10):
    if n==4:
        break
    print(n)

#exemplo com continue
#vai pular o numero 4
for n in range(0, 10):
    if n==4:
        continue
    print(n)
