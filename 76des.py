l=('Tinta guache grande','20,99'
 ,'Caderneta para recados','15,99',
 'Lápis preto 6B','5,60',
 'Borracha','2,71',
'Folhas sulfite 60 A4','32,00',
 'Folhas sulfite 60 A3',
 'Cola grande branca líquida','9,99',
  'Pincel chato nº 0','11,45',
 'Pincel chato nº 14','11,45',
'Pasta de aba elástica','7,67',
 'Apontador','1,35',
 'Caixa de giz de cera curto','45,00',
 'Conjunto de lápis de cor','12,89',
 'Estojo','22,80',
 'Caixas de massa de modelar 12 cores','6,73',
 'Tesoura sem ponta​','7,00')
for p in range(0,len(l)):
    if p %2==0:
        print(f'{l[p]:.<30}')
    else:
        print(f'R${l[p]:>7}')