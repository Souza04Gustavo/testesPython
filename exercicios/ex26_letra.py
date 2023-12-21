#analisando uma letra no nome de alguem
nome = input('Digite seu nome: ').strip()
letra = 'A'
print('Total de letras ''{}'': {}'.format(letra, nome.upper().count('A')))
print('Primeira posição de ''{}'': {}'.format(letra, nome.upper().find('A')))
print('Ultima posição de ''{}'': {}'.format(letra, nome.upper().rfind('A')))