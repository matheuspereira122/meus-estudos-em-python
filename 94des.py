galera=[]
pessoa={}
while True:
    pessoa.clear()
    pessoa['nome']=str(input('nome:'))
    while True:
        pessoa['sexo']=str(input('sexo [M/F]:')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO voce digitou um sexo sem ser masculino ou feminino')
    pessoa['idade']=int(input('idade:'))
    galera.append(pessoa.copy())
    while True:
        r=str(input('quer continuar')).upper().strip()[0]
        if r not in 'SN':
            print('digite novamente')
            break
    if r =='N':
         break