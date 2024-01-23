n=int(input('digite um numero'))
n1=int(input('digite um outro numero'))
op=0
while op !=5:
    print('''[1] SOMA
[2] MULTIPLIÇÃO
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PRPGRAMA''')
    op=int(input('qual sua opcição'))
    if op ==1:
        print( 'a soma é{}'.format(n1+n))
    if op==2:
        print('a multiplicação é {}'.format(n1*n))
    if op==3:
        maior=n
    else:
        maior=n1
    print('o maior é {}'.format)
    if op==4:
        n=int(input('digite o primeiro numero'))
        n1=int(input('digite o segundo numero'))
    else:
        print ('tente novamente erro')
print('final do programa')