from datetime import date
ano=int(input('qual ano vc quer analizar?'))
if ano==0:
    ano= date.today().year
if ano % 4==0 and ano % 100 != 0 or ano % 400==0:
    print('é bisexto')
else:
    print('um ano normal')