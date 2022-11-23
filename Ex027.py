'''Faça um programa que leia uma frase pelo teclado e mostre:
quantas vezes aparece a letra A
Em que posição ela aparece a primeira vez
em que posição ela aparece a última vez'''
frase = str(input('Digite a frase: ')).strip().lstrip()
qnt = frase.upper().count('A')
print ("A letra 'a' apareceu {} vezes na frase! \nA primeira letra 'a' foi encontrada na posição {}!".format(qnt,frase.lower().find('a')))
print ('A ultima posição encontrada foi: {}'.format(frase.lower().count('a',0,(len(frase)))))