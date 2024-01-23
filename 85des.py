lista=[]
par=[]
inpar=[]
for c in range(8):
    n=int(input('digite um valor'))
    if n%2==0:
        par.append(n)
    if n%2==1:
        inpar.append(n)
    
lista.append(par)
lista.append(inpar)
print(f'os numeros digitados foram{lista}')
print(f'os numeros pares foram{lista[0]}')
print(f'numeros ipares {lista[1]}')
