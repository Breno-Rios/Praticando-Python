'''
Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. 
Isso ajudará a analisar a estrutura das palavras utilizadas.

Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

Exemplo de entrada:

Digite um texto: A linguagem Python é muito versátil.  
Copiar código
Saída esperada:

O texto contém 13 vogais.
'''

import re

def contar_vogais(texto):
  soma = 0
  vogais = 'aeiou'
  for a in texto:
    if a in vogais:
      soma+=1
  return soma

def main():
  texto = input('Digite um texto: ').lower()
  print(f'O texto contém {contar_vogais(texto)} vogais.')

main()