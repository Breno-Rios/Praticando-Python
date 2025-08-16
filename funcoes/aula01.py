'''
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento.
 Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.

Exemplo de entrada:


Digite o ano de nascimento: 2005  

Digite o ano atual: 2025 
Copiar código
Saída esperada:


A idade é 20 anos. 
'''
def idade (ano_nascimento, ano_atual):
  idade = ano_atual - ano_nascimento
  return print(f'A idade é {idade} anos.')

nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))

idade (nascimento, ano_atual)

