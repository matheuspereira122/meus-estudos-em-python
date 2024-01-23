def maior (*num):
    cont=maior=0
    print(' /nanalisando numeros...')
    for valor in num:
        print(f'{valor}', end='')
        if cont==0:
            maior=valor
        if valor>maior:
            maior=valor
        cont+=1
    print(f'foi {cont} valores')
    print(f'o maior {maior}')

maior (2, 9, 4, 5, 7 , 1)
maior (4, 7 , 0)
maior (1 ,2 )
maior (6)
maior()