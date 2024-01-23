num=[]
i=[]
p=[]
while True:
    num.append(int(input('digite um numero')))
    r=str(input('quer continuar[S/N]')).upper().strip()[0]
    if r=='N':
        break
for l,v in enumerate(num):
    if v % 2==0:
        p.append(v)
    if v %2==1:
        i.append(v)
print(f'a lista completa é {num}')
print(f'a lista de numeros pares é `{p}')
print(f'a lista de numeros ipares {i}')
