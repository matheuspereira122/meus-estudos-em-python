from random import randint
def sorteia():
    for cont in range(0,5):
        n=(randint(1,10))
        numeros.append(n)
        print(f'{n}', end='')
def somapar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
            print(f'os pares de {lista}, temos {soma}')
numeros=list()
sorteia(numeros)
print(numeros)
somapar(numeros)