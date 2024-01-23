s1='M'
s2='S'
n=str(input('digite o seu saxo M/F?')).strip().upper()
while n not in 'M'  'F':
    n=str(input('digite corretamente'))
if n==s1:
    print('sexo masculino resgistrado')
elif n==s2:
    print('sexo feminino registrado com sucesso')