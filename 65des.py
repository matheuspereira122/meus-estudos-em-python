r1='S'
s=0
q=0
m=0
maior=0
menor=0
while r1 in 'S':
    n=int(input('digiti um nuemro'))
    s+=n
    q+=1
    r1=str(input('quer continuar?')).upper().strip()[0]
    if q ==1:
        menor=maior =n
    if n>maior:
        maior=n
    if n<menor:
        menor=n
m=(s/q)
print('voce usou {} numeros, a media dels foi {}, e a soma entra eles foi {}, o menor numero {}, e o maior{}'.format(q,m,s,menor,maior) )
