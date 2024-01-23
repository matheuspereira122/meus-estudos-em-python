t=int(input('digite o seu termo'))
r=int(input('digite sua razão'))
t1=t
c=1
total=0
m=10
while m !=0:
    total=+total+m
    while c <=total:
        print('{}'.format(t))
        t+=r
        c+=1
print('PAUSA')
m=int(input('quantos a amsi vc quer mostrar'))
print('FIM')