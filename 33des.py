a=int(input(' degite um numero'))
b=int(input('digite outro numero'))
c=int(input('digite outro numero'))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
print('o menor é{}'.format(menor))