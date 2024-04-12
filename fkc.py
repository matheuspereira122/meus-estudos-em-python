while True:
    # TODO: write code...
    r=int(input('''qual converçao voce quer fazer?
    digite 1 para celsius
    2 para fahrenhein
    3 para kelvins'''))
    if r ==1:
        c=float(input('temperatura em celcius'))
        fc=c*1.8 + 32
        kc=c+273
        print(f'C°={c}')
        print(f'F°{fc}')
        print(f'K°{kc}')
    elif r == 2:
        f=float(input('temperatura em fahrenhein'))
        cf=f-32 /1.8
        kf=((f-32/9) *5)+273
        print(f'F°={f}')
        print(f'C°={cf:.2f}')
        print(f'K°={kf:.2f}')
    elif r== 3:
        k=float(input('temperatura em kelvins'))
        ck=k-273
        fk=(((k-273)/5)*9)+32
        print(f'K°={k}')
        print(f'C°={ck:.2f}')
        print(f'F°={fk:.2f}')
    r1=int(input('quer continuar?[1 para sim/e 2 para nao]'))
    if r1 ==2:
        break
    