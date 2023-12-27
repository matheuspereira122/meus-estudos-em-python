print('lojas mordrgous')
v=int(input('digite o valor'))
print('''opiçoes de pagamento
      [1] dinheiro /cheque
      [2] cartâo total
      [3] cartão 2x
      [4] cartão 3x ou mais''')
r=int(input('qual é a forma de pagmento? '))
if r==1:
    vf=float(0.1*v)
    print('o valor é{}'.format(vf))
elif r==2:
    vfc=float(0.05*v)
    print('vai ficar {}'.format(vfc))
elif r==3:
    vv=float(v/2)
    print( 'vai ficar uma parce3la de {}, e outra de{}'.format(vv,vv))
elif r==4:
    p=int (input("quantas parcelas?"))
    ufc= float(v/p)
    wwe=float(p*0.2)
    vvv=float(ufc*wwe)
    print('sera no total de parcelas mensais de {}'.format(vvv))
print('obrigado, volte sempre!!!')