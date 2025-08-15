'''
Digite o nome do produto: Caneta 

Digite a quantidade: 50 

Digite o nome do produto: Caderno 

Digite a quantidade: 30 

Digite o nome do produto: Borracha 

Digite a quantidade: 20 

Dicionário de produtos: {'Caneta': 50, 'Caderno': 30, 'Borracha': 20} 
'''
dict_produtos = {}
i=0
while i < 3:
  produto = input('Digite o nome do produto: ')
  qntd = input('Digite a quantidade: ')
  dict_produtos[produto]= qntd
  i+=1

print(f'Dicionário de produtos: {dict_produtos}')