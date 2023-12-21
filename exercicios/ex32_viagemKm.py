km = float(input('Insira a distancia da viagem (Km): '))
if km <= 200:
    valor = km * 0.5
    print('Pagará: {} reais'.format(valor))
else:
    valor = km * 0.4
    print('Pagará: {} reais'.format(valor))