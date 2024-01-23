lista=[]
while True:
    n=int(input('digite um numero'))
    lista.append(n)
    print('-='*30)
    r=str(input('quer continuar[S/N?]')).upper().strip()[0]
    if r=='N':
        break
    print('-='*30)

print('-'*30)
print(f'essa listas tem {len(lista)} valores')
print('-'*30)
lista.sort(reverse=True)
print(f'em ordem decresent{lista}')
print('-'*30)
if 5 in lista:
        print('o valor 5 esta na lista')
else:
     print('o valor 5 nao esta na lista')
