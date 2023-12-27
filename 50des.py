s=0
c=0
for p in range (1, 7):
    n=int(input('digiye um numero'))
    if n %2==0:
        s+= n
        c+=1
print('voce informou{} numeros e a soma foi {}'.format(c,s))