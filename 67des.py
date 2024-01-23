print('TABUADA')
while True:
    n=int(input('qual tabuada voce quer saber?'))
    if n<0:
        break
    for c in range (1,11):
        r=int(n*c)
        print(f'{n} X {c} = {r}')
