'''
Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. 
Essa verificação será usada para definir ações diferentes dentro do jogo. 
Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.
'''
numero = int(input('Digite um número: '))

resto = numero % 2

if resto == 0:
    print('PAR')
else:
    print('ÍMPAR')

