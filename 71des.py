print('caixa eletronico')
v=int(input('qual o valor q vc deseja sacar'))
t=v
ced=50
tc=0
while True:
    if t>=ced:
        t-=ced
        tc+=1
    else:
        print('total de cedulas{}, total de r${}'.format(tc,ced))
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        if ced==10:
            ced=1
        if t==0:
            break