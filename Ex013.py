#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Digite o valor do produto: R$ '))
print('Com 5% de desconto, o preço fica em R$ {:.2f}'.format(valor-(valor*0.05)))

#OUTRA FORMA DE RESOLVER
#valor = float(input('Digite o valor do produto: R$ '))
#novo = valor - (valor * 5 / 100)
#print('Com 5% de desconto, o preço fica em R$ {:.2f}'.format(novo))