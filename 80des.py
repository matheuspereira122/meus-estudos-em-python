lista=[]
for c in range(0, 5):
    n=int(input('digite um numero'))
    if c==0 or n>lista[-1]:
        lista.append(n)
    else:
        pos=0
        while pos <= lista[pos]:
            if n<=lista[pos]:
                lista.insert(pos, n)
                break
            pos+=1
print('-='*30)
print(f'a ordem certa é {lista}')