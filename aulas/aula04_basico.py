print('--- AULA 04 PYTHON MUNDO 1 ---')

nome = input('Digite seu nome completo: ')
print('Boas vindas', nome, '!!!')

idade = int(input('Digite a sua idade: '))
altura = float(input('Digite sua altura: '))

print('Seu nome é:', nome, '\nSua idade é:', idade, 'anos', '\nSua altura é:', altura, 'metros' )

dia = int(input('Insira o dia do seu nascimento: '))
mes = int(input('Insira o mes do seu nascimento: '))
ano = int(input('Insira o ano do seu nascimento: '))

print('Voce nasceu no dia {}/{}/{}'.format(dia, mes, ano))

print('*** TESTE DE SOMA ***')

a = int(input('Insira um inteiro: '))
b = int(input('Insira outro inteiro: '))
c = a + b

print('A soma de ambos é ', c)