boletim={}
boletim ['nome']=str(input('digite o nome do aluno'))
boletim ['nota']=float(input('digite a media do aluno'))
if boletim['nota']<5:
    print(f'{boletim["nome"]} teve a nota de {boletim["nota"]}e foi reprovado')
if boletim['nota']>5:
    print(f'{boletim["nome"]}foi aprovado com a nota de {boletim["nota"]}')