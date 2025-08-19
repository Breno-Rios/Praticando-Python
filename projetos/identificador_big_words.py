'''
Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. 
Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.

Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. 
Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

Exemplo de entrada:

Digite um texto: A programação estruturada facilitou o desenvolvimento de grandes sistemas computacionais
Copiar código
Saída esperada:

Palavras longas encontradas: programação, estruturada, desenvolvimento, computacionais 
Copiar código
Se nenhum palavra longa for encontrada:

Nenhuma palavra longa foi encontrada no texto. 
'''

texto = input('Digite um texto: ').split()
palavras = []

for t in texto:
  if len(t)> 10:
    palavras.append(t)

if len(palavras) ==0:
  print('Nenhuma palavra longa foi encontrada no texto.')
else:
  print(f'Palavras longas encontradas: ')
  for p in palavras:
    print(p)
  
