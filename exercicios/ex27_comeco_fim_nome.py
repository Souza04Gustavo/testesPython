#selecionando somente o primeiro e ultimo nome de uma pessoa
nome = input('Digite seu nome: ').strip()
nome_lista= (nome.split())
print('Seu primeiro nome: {}'.format(nome_lista[0]))
tamanho = len(nome_lista)
print('Seu ultimo nome: {}'.format(nome_lista[tamanho - 1]))