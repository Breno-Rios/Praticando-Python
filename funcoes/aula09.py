'''
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.

Exemplo de entrada:


Digite a porcentagem de desconto: 10 

Digite o valor da compra: 200 
Copiar código
Saída esperada:


Preço final com desconto: 180.0
'''

def valor_compra(valor):
  def desconto(percent):
    return valor - (percent/100)*valor
  return desconto

total = float(input('Digite o valor da compra: '))
percent = int(input('Digite a porcentagem de desconto: '))

total_compra =valor_compra(total)

print(f'Preço final com desconto: {total_compra(percent)}')
