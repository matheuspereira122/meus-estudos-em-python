print('LOJAS ZLANTANS')
t=0
mil=0
b=0
c=0
b1=''
while True:
    n=str(input('qual o nome do pruduto'))
    p=float(input('qula o preço do produto?'))
    c+=1

    t+=p
    if p>1000:
        mil=1
    if c==1:
        b=p
        b1=n
    if p<b:
        b=p
        b1=n
    r=str(input('quer continuar [S/N]?')).upper().strip()[0]
    if r=='N':
        print('obrigado volte sempre')
        break
print('voce gastou no total R${} com {} prudutos acima de 1000 reais e o mais barato foi {} que custa R${}'.format(t,mil,b1,b))