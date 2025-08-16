'''
Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

Exemplo de entrada:


Digite uma palavra: tecnologia 
Copiar código
Saída esperada:


Essa palavra tem 10 caracteres. 
'''

def tamanho_palavra(str):
  caracteres = len(str)
  return print(f'Essa palavra tem {caracteres} caracteres.')

palavra = input('Digite uma palavra: ')
tamanho_palavra(palavra)