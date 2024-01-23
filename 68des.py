from random import randint
v=0
while True:
    j=int(input('digite um numero de 1 a 10'))
    c=randint(0,11)
    total=int(j+c)
    tipo=''
    while tipo not in 'PI':
        tipo=str(input('par ou inpar[P/I?]')).upper().strip()[0]
    if tipo=='P':
         if tipo%2==0:
             print(' voce venceu')
             v+=1
        else:
            print('voce perdeu')
            break
    elif tipo =='i':
        if tipo%2==1:
            print('voce ganhou')
            v+=1
        else:
            print('voce perdeu')
            break