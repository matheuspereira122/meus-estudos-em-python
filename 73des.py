br1='1°Palmeiras','2°Gremio','3°Atletico-MG','4°Flamengo','5°Botago','6°Bragantino','8°Athletico-PR','9°Internacional','10°Fortaleza','12°Cuiabá','13°Corinthians','14°Cruzeiro','15°Vasco da Gama','16°Bahia','17°Santos','18°Goiás','19°Coritiba','20°America-MG'
br2='Palmeiras','Gremio','Atletico-MG','Flamengo','Botago','Bragantino','Fluminese','Fluminense','Athletico-PR','Internacional','Fortaleza','São Paulo','Cuiabá','Corinthians','Cruzeiro','Vasco da Gama','Bahia','Santos','Goiás','Coritiba','America-MG'
f=str('Fluminense Campeao da Libertadores')
s=str('São Paulo Campeao da Copa do Brasil')
while True:
    print('''Qual informaçoes voce quer saber
      [1] O CAMPEAO
      [2] OS MEMBROS DO G4
      [3] OS CLASIFICADOS PARA A COMEBOL LIBERTADORES DA AMERICA
      [4] OS CLASSIFICADOS PARA COMEBOL SULAAMERICANA
      [5] OS 4 REBAIXADOS PARA SERIE B
      [6] QUERO SAIR DO PROGRAMA
      [7] QUERO ELES EM ORDEM ALFABETICA
      [8] EM QUAL POSIÇAO ESTA O CORINTHINAS''')
    r=int(input('qual a sua opçao'))
    if r==1:
        print(br1[:1])
    if r==2:
        print(br1[0:4])
    if r==3:
        print(br1[0:6])
        print('{} e o {}'.format(f,s)) 
    if r==4:
        print(br1[7:13])
    if r==5:
        print(br1[16:19])
    if r==6:
        break
    if r==7:
        print(sorted(br2))
    if r==8:
        print(br1[10])