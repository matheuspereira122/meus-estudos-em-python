Peso=float(input('seu peso?'))
Altura=float(input('sua altura?'))
imc=Altura*Altura /Peso
if imc<=18.5:
    print(' vc esta a baixo do peso')
elif imc<=25.0:
    print('peso ideal')
elif imc<=30.0:
    print('sobreso')
elif imc<=40:
    print('obsendade')
elif imc>40:
    print('obesidade morbida')