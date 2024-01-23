temp=[]
prin=[]
ma=0
me=0
while True:
    temp.append(str(input('digite o nome')))
    temp.append(float(input('digite o peso')))
    if len(prin)==0: 
        ma=me=temp[1]
    if temp[1]> ma:
        ma=temp[1]
    if temp[1]< me:
        me=temp
    r=str(input('quer continuar')).upper().strip()[0]
    prin.append(temp[:])
    temp.clear
    if r=='N':
        break
print('-='*30)
print(f'{len(prin)}')
print('-='*30)
for p in prin:
    if p[1]==ma:
        print(f'[{p[0]}]')
for p in prin:
    if p[1]==me:
        print(f'{p[0]}'])