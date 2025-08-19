'''
Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. 
O CPF deve conter exatamente 11 dígitos numéricos. 
Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.

Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.

Exemplo de entrada:

Digite seu CPF: 12345678901
Copiar código
Saída esperada:

CPF válido.
Copiar código
Se for inválido:

Digite seu CPF: 1234abc567  
Erro: O CPF deve conter apenas números.  
Copiar código
Se o CPF tiver um número de dígitos diferente de 11:

Digite seu CPF: 1234567  
Erro: O CPF deve ter exatamente 11 dígitos.
'''
import re 
input_cpf= input('Digite seu CPF: ')

if not re.fullmatch(r'\d*', input_cpf):
  print('Erro: O CPF deve conter apenas números.')
elif(len(input_cpf) != 11):
  print('Erro: O CPF deve ter exatamente 11 dígitos.')
else:
  print('CPF válido')