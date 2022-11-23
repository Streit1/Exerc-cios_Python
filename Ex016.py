#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
#Calcule o preço a pagar,sabendo que o carro custa R$ 60,00 pr dia e R$ 0,15 por KM rodado
km = float(input('Digite a quantidade de Km rodados: '))
d = int(input('Digite a quantidade de dias que utilizou o carro: '))
tkm = float(km*0.15)
td = d * 60
print('Extrato:\nQuilometragem rodada: {:.3f}\nValor pago pela Quilometragem: R$ {:.2f}\nQuantidade de dias utilizados: {}\nValor pago por dia: R$ {:.2f}\nVALOR TOTAL: R${:.2f}'.format(km,tkm, d, td,(tkm +td)))
