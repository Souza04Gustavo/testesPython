#se passar de 80km/h pagará 7 reais por Km
v = float(input('Insira a velocidade do veiculo: '))
if v > 80:
    multa = (v - 80)*7
    print('Multado em {} reais!'.format(multa))