'''
João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. 
O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.

Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.

Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta. O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.

Exemplo de entrada:

Digite o valor da conta: 120.00  
Digite a porcentagem de gorjeta: 10  
Copiar código
Saída esperada:

Valor da gorjeta: R$ 12.00  
Total a pagar: R$ 132.00
'''

def calcular_gorgeta(conta,porcentagem):
  gorgeta=conta*(porcentagem/100)
  return gorgeta

def total_conta(conta,gorgeta):
  return conta + gorgeta

def main():
  conta = float(input('Digite o valor da conta: '))
  porcentagem = int(input('Digite a porcentagem de gorjeta: '))

  gorgeta= calcular_gorgeta(conta,porcentagem)
  total = total_conta(conta,gorgeta)

  print(f'Valor da gorjeta: R$ {gorgeta: .2f}')
  print(f'Total a pagar: R$ {total: .2f}')


main()