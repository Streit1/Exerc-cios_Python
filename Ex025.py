'''Crie um programa que receba o nome de uma cidade e diga se ela começa ou não com o nome SANTO'''
cidade = str(input('Digite o nome da cidade: ')).strip() #recebe o nome e já remove os espaços se houver
dividido = cidade.upper().split() #Coloca todos as strings em caixa alta e divide a frase
print(dividido[0] == 'SANTO') #analise se a primeira palavra em caixa altaficou igual a solicitada
#print(dividido[0])
