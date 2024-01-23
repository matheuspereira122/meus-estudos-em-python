n=[]
ma=0
me=0
for c in range(0,5):
    n.append(int(input(f'digite um valor na posiçao {c}')))
    if c==0:
        ma=me=n[c]
    if n[c]>ma:
        ma=n[c]
    if n[c]<me:
        me=n[c]    
for i, v in enumerate(n):
    if n[i]== max(n):
        print(f'o maior valor foi {max(n)}, digitado na posiçao {i+1}')

for i,v in enumerate(n):
    if n[i]==min(n):
        print(f' omenor digita foi {min(n)}, na posiçao {i+1}')