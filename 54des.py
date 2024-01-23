from datetime import date
atual=date.today().year
for p in range(1,8):
    na=int(input('qual é o nacimento?'))
    i= atual-na
    if i>18:
        print('essa pessoa é de maior com {} anos '.format(i))
    else:
        print ('essa pessoa é de menor com {}anos '.format(i))