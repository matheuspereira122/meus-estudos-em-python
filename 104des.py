def leiaint(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok=True
            break
        else:
            print('isso nao é um numero')
    return valor  
n=leiaint('digite um nuemro')
print(f'voce acabou de digitar o numero {n}')