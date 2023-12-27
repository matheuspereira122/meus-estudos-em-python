n1=float(input('digite a primeira nota do seu aluno'))
n2=float(input('digite a segunda nota'))
nome=input('digite o nome completo')
nota=float (n2+n1)/2
if nota==10:
    print('o aluno {}, foi aprovado com grande sucesso pois tirou nota maxima'.format(nome) )
elif nota >= 7:
    print('o aluno{} foi aprovado com um bom aproveitamento'.format(nome))
elif 5>=nota:
    print('o aluno {}pasou na media busque melhoras'.format(nome))
elif nota<=4:
    print('o aluno {} foi reprovado'.format(nome))