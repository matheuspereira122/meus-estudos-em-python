import random
n1=int(0)
n2=int(1)
n3=int(2)
n4=int(3)
n5=int(4)
n6=int(5)
numero=[n1,n2,n3,n4,n5,n6]
random.shuffle(numero)
nu=int(input('digite um numero de 0 a 5'))
if nu==numero:
    print('vc acertou o numero')
else:
      print('vc é burro vc erou o numero ')