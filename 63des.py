n1=int(input('quantos termos vc quer mostrar?'))
t1=0
t2=1
print('''
{}
{}'''.format(t1,t2))
c=3
while c<=n1:
    t3=t1+t2
    print('{}'.format(t3))
    t1=t2
    t2=t3
    c+=1
print('ACABOU A PALHAÇADA')