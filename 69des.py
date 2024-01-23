print('PROGRAMA DE ANALISE DE DADOS')
print('________________________________________________________________________________')
print('CADASTRE UMA PESSOA')
c=0
mid=0
H=0
MF=0
F=0
MM=0
while True:
    i=int(input('IDADE?'))
    if i>=18:
        mid+=1
    s=str(input('[M/F]?')).upper().strip()[0]
    if s =='M':
        H+=1
    if s=='F':
        F+=1
        if i>=20:
            MM+=1
    r=str(input('QUER CONTINUAR?[S/N]')).upper().strip()[0]
    c+=1
    if r=='N':
        print('OBRIGADO POR ME USAR')
        break
mmm=int(mid-MM)
print(' VOCE REGISTOU {} maiores de idade, {} Homens e {} mulheres com de 20'.format(mid,H,mmm))