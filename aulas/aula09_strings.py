frase = '  Aprendendo Python no curso gratuito  '
print(frase[0], frase[2])

print('''Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o 
Fatiamento de String, Análise com 
len(), count(), find(), transformações com replace(), 
upper(), lower(), capitalize(), title(), strip(), 
junção com join().''')

print(frase.count('o'))
print(frase.upper())
print(len(frase))
print(len(frase.strip()))

frase = frase.strip().replace('Python', 'python')
print(frase)
print('curso' in frase)
print(frase.find('curso'))

divido = frase.split()
print(divido)
print(divido[1])
print(divido[1][0])
