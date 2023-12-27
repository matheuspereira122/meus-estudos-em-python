n1=int(input('digite um numero'))
n2=int(input('digite um outro numero'))
r=int(n1-n2)
if r==0:
    print('esses numeros são iguais')
elif n1>n2:
    print('o primeiro valor é maior com diferença de {}'.format(r))
elif n2>n1:
    r1=int(n2-n1)
    print('o segundo valor é maior com a diferença de {}'.format(r1))