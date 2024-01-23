jogador={}
partida=[]
jogador['nome']=str(input('nome:'))
tot=int(input('quantas partidas ele jogou'))
for c in range(0,tot):
    partida.append(int(input(f'quantos gols em {c} partidas')))
jogador['gols']=partida[:]
jogador['total']=sum(partida)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-='*30)
print(f'jogador {jogador["nome"]}, jogou {len(jogador['gols'])}')
for i, v in enumerate(jogador['gols']):
    print(f'   =>na partida {i},fez {v} gols')
print(f'no total de {jogador["total"]} de gols')