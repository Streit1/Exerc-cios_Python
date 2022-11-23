n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 = n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 **n2
print('A soma e {}, o produto é {}, e a divisão é {:.2f}'.format(s,m,d), end=' ')#{:.3f} é a formatação de quantas casas ficam depois da vírgula, o ,end' ' é o comando para imprimir o que está abaixo na mesma linha
print('Divisão inteira {} e potência {}'.format(di,e))
