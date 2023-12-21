import random
num = random.randint(0,5)
chute = int(input('Adivinhe o numero que o computador pensou: '))
if chute == num:
    print('Isso!!!')
else:
    print('ERROU!!! O numero era {}'.format(num))