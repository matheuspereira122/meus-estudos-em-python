p=('escalaçao','comprobante','servitude','oferecimento','arguida','pulsaçao','parafiscal','lupus','superalimentar','catamara')
for pa in p:
    print(f'na palavra {pa}')
    for l in pa:
        if l.lower() in 'aeiou':
            print(l, end='')