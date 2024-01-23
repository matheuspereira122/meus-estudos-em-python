maior=0
manor=0
for c in range(1,6):
    p=int(input('qual é o pesso da {} pessoa?'.format(c)))
    if p==1:
        maior=p
        menor=p
    else:
        if p>maior:
            maior=p
        if p<maior:
            menor=p
print('o pessoa maior foi {}'.format(maior))
print('o menor peso foi {}'.format(menor))
