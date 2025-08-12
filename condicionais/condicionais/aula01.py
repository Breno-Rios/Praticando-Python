
'''
Monitorando vendas no comércio

Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. 
Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. 
Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. 
Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
'''

apple = int(input('Digte a quantidade de Maçãs vendidas: '))
banana = int(input('Digte a quantidade de Bananas vendidas: '))

if apple > banana:
    print('As maças tiveram mais vendas.')
elif apple < banana:
    print('As bananas tiveram mais vendas.')
else:
    print('As ambas tiveram vendas iguais.')