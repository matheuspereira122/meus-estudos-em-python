from datetime import datetime
trabalhador={}
while True:
    trabalhador['nome']=str(input('nome:'))
    nascimento=int(input('data de nascimento:'))
    trabalhador['numero da carteira de trabalho']=int(input('carteira de trabalho(0 nao tem)'))
    if trabalhador['numero da carteira de trabalho']==0:
        break
    trabalhador['idade']=datetime.now().year-nascimento
    trabalhador['ano']=int(input('tempo de trabalho:'))
    trabalhador['salario']=int(input('salario:'))
    trabalhador['aposentadoria']=trabalhador['idade']+((trabalhador['ano']+35)-datetime.now().year)
    break
print('-='*30)
for k,v in trabalhador.items():
    print(f'-{k} tem o valor{v}')

