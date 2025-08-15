'''
Clara é editora de uma revista e deseja comparar dois artigos para identificar quais palavras aparecem em ambos.
 Sua tarefa é criar um programa que receba dois textos e exiba o conjunto de palavras comuns entre eles.

Exemplo de entrada:


Texto 1: O sol brilha forte no céu azul 

Texto 2: O céu azul anuncia um dia de sol intenso 
Copiar código
Saída esperada:


Palavras em comum: {'o', 'azul', 'sol', 'céu'} 
'''

texto1 = set(input('Texto 1: ').lower().split())
texto2 = set(input('Texto 2: ').lower().split())

intersection = texto1&texto2
print(f'Palavras em comum: {intersection} ')