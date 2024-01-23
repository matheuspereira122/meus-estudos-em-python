si=0
mi=0
mh=0
mv=''
for p in range(1,5):
    print('_____{}° pessoa______'.format(p))
    nome=str(input('digite o nome ')).strip()
    idade=int(input('digite a idade'))
    sexo=str(input('digite o sexo')).strip()
    si+=idade
    if p== 1 and sexo=='Mm':
        mh=idade
        mv=nome
    if sexo in 'Mm' and idade>mh:
        mh=idade
        mv=nome
mi=si/4
print('a media de idade é de {} anos'.format(mi))
print('o homem mais velho com {} anos, e o seu nome é {}'.format(mh,mv))