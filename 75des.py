n=(int(input('digite um numero')),int(input('digite mais um numero')),int(input('digite um outro numero')),int(input('digite o ultimo')),)
print('voce digitou os valores {}'.format(n))
if 9 in n:
    print(f' o valor 9 apareceu {n.count(9)}')
if 3 in n:
    print(f' o valor 3 apareceu{n.index(3)+1} POSIÇAO')
for nu in n:
    if nu % 2==0:
         print(f'O VSALORES PARES {nu}')
