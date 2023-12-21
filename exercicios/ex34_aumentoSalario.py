s = float(input('Insira o salario: '))
if s > 1250:
    s = s*1.1
    print('Com aumento seu salario atual é: {:.2f} reais'.format(s))
else:
    s = s*1.15
    print('Com aumento seu salario atual é: {:.2f} reais'.format(s))
