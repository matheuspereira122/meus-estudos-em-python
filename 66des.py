n=0
c=0
s=0
while True:
    n=int(input('digite um numero'))
    s+=n
    c+=1
    if n==999:
        break
print(' voce usou {} veses e a soma deu {}'.format(c-1,s-999))