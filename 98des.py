from time import sleep
def contador(i, f, p):
    if i <f:
        cont=i
        while cont<=f:
            print(f'{cont},', end='', flush=True)
            cont+=p
            sleep(1.0)
        print('  FIM.  ')
    if p<0:
        p*-1
    if p==0:
        p=1
    else:
        cont=i
        while cont>=f:
            print(f'{cont},',end='',flush=True)
            cont-=p
            sleep(1.0)
        print('  FIM.  ')
contador(1,10,1)
contador(10,0,2)
print('agora é sua vez de personalizar a contagem')
ini=int(input('digite'))
fim=int(input('digite'))
pas=int(input('digite'))
contador(ini,fim,pas)