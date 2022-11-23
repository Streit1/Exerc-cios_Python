'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem  o primeiro nome'''


nome = str(input('Digite seu nome completo: '))
print('Seu nome completo é: {}'.format(nome))
letras = len(nome) #retorna o tamanho de nome


#nome.count('o') #função que vai contar quantas vezes tem o 'o' em nome
#nome.count('o',0,13) ''' Verifica quantas letras 'o' tem da posição zero até 13''
#nome.find('deo') #verifica onde começo 'deo'
#nome.upper() Coloca todas as Strings em letra maiúscula
#nome.lower() Coloca todas as Strings em letra minúscula
#nome.capitalize() Coloca todas as Strings em letra minúscula e deixa somente a primeira letra em caixa Alta
#nome.title() Transforma cada início de palavra em letra maiúscula
#nome.strip() remove todos os espaços no início e no final da String (espaços excedentes)
#nome.rstrip() remove somente os últimos espaços
#nome.lstrip() remove somente os espaços da esquerda
#nome.split() divide a frase (onde tem espaços) gerando uma lista com todas as palavras divididas.
#'-'.join(nome) junta as palavras em uma frase colocando um '-' para dividir
