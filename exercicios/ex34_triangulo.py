a = float(input('Lado 1: '))
b = float(input('Lado 2: '))
c = float(input('Lado 3: '))
if a < b + c and b < a + c and c < b + a:
    print('É triangulo!!!')
else:
    print('Não é triangulo!!!')
