num=int(input('digite um numero inteiro'))
print('''digite uma opçao
      [1] numero binario
      [2] numero octal
      [3] numero hexadecimal''')
opição= int(input('sua opção'))
if opição == 1:
    print('{}'.format(bin(num)))
elif opição==2:
    print('{}'.format(oct(num)))
elif opição==3:
    print("{}".format(hex(num)))
else:
    print('opção ivalida')