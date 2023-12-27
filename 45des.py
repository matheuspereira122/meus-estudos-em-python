import random
print('''Bem-vindo a o jogo!!!
      [1] TESOURA
      [2] PEDRA
      [3] PAPEL''')
r=int(input('qual é a sua jogada?'))
if r==1:
    print('pedra eu ganhei')
elif r==2:
    print ('teusoura eu perdi')
elif r==3:
    print('eu perdi')