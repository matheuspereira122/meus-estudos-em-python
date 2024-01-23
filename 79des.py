num=[]
while True:
    n=int(input('digite outro numero'))
    r=str(input('voce quer continuar[S/N]?')).upper().strip()[0]
    if n not in num:
        num.append(n)
        print('numero adicionado com sucesso')
    else:
        print('duplicado nao vou adicionar')
    if r =='N':
        break
num.sort()
print(f'voce digitou os valores {num}')