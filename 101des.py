from datetime import date
def voto(nas):
    atual=date.today().year
    nas=atual-nas
    if nas<16:
     print(f'com {nas}anos seu voto é negado')
    if nas==17:
       print(f'o voto com {nas} anos,é opicional')
    if nas >=18:
       print(f'com {nas} o voto é obrigatorio')
    if nas>>75:
       print(f'com {nas}anos seu voto é opicional ')
nas=int(input('que ano vc nasceu?'))
voto(nas)