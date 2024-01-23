n= int(input('digite um numero'))
for c in range(1, n+1):
    if n % c==0:
        print(' divisivel')
    else:
        print('nao divisivel')
    print('{}'.format(c))