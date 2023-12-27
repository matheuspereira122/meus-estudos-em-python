km=float(input(' qual é a kilomentragem da viagem'))
v=float(km*0.50)
v2=float(km*0.45)
if km >=200:
    print(' sua viagem custa R${}'.format(v2))
if km <= 200:
    print('sua viagem custa R${}'.format(v))