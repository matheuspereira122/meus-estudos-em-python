def ficha(jog,gol=0):
    print(f'o jogador {n}, marcou {g} gols')
n=str(input('nome do jogador:'))
g=str(input('quantidade de gols:'))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)
