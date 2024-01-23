from random import randint
n=randint(0,10)
p= False
pal=0
while  not p:
    j=int(input('digite um nuemro de 0 a 10'))
    pal+=1
    if j==n:
    
        p=True
    elif j>n:
        print('menos')
    elif j<n:
        print('mais')
print('voce acertou {}, com {} tentativas'.format(n,pal))