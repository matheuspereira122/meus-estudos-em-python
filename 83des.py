expr=str(input('digite uma expresão'))
pilha=[]
for simb in expr:
    if simb=='(':
        pilha.append('(')
    if simb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
        break
if len(pilha)==0:
    print('expresão esra valida')
else:
    print('sua expresão esta errada')
