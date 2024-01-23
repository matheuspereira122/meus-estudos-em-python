time=[]
jogador={}
partida=[]
while True:
    jogador.clear()
    jogador['nome']=str(input('nome:'))
    tot=int(input('quantas partidas ele jogou'))
    partida.clear()
    for c in range(0,tot):
        partida.append(int(input(f'quantos gols em {c} partidas')))
    jogador['gols']=partida[:]
    jogador['total']=sum(partida)
    time.append(jogador.copy())
    while True:
        r=str(input('continuar?')).upper().strip()[0]
        if r=='N':
            break
    if r=='N':
        break
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.valunes():
        print(f'{str(d):>15}', end='')
print('-='*30)
print(f'jogador {jogador["nome"]}, jogou {len(jogador['gols'])}')
for i, v in enumerate(jogador['gols']):
    print(f'   =>na partida {i},fez {v} gols')
print(f'no total de {jogador["total"]} de gols')