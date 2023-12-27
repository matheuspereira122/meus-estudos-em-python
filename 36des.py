s=int(input('qual é o seu salario?'))
v=int(input('qual é o valor da casa?'))
t=int(input('quantos anos vc ira pagar?'))
p=int(s*30/100)
p1=int(v/t)/12
if p>p1:
    print('voce pagara por {} anos,R${}por mes '.format(t,p1))
elif p1>p:
    print('voce nao pode pagar essa pois a quantidade de tempo de {} anos ecede mais de 30% do seu salario'.format(t))
