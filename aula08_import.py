#estudando e aplicando imports

import random
num = random.randint(1, 1000)
print(num)

import math
#from math import sqrt
#raiz = sqrt(num)
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}'.format(num, raiz))
#arredondando para baixo um valor
print('A raiz arredondada para baixo é {}'.format(math.floor(raiz)))
#arredondando para cima um valor
print('A raiz arredondada para cima é {}'.format(math.ceil(raiz)))
