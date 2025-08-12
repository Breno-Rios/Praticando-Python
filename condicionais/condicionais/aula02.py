'''
Calculando o tempo total de projeto

Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. 
No entanto, se alguma atividade tiver um número de dias negativo, 
o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. 
Se algum valor for negativo, mostre uma mensagem informando o erro.

'''

atividadeA = int(input('Informe os dias para a atividade A: '))
atividadeB = int(input('Informe os dias para a atividade B: '))
atividadeC = int(input('Informe os dias para a atividade C: '))

if(atividadeA<0 or atividadeB<0 or atividadeA<0):
    print("Erro: os dias não podem ser negativos.")
else:
    total= atividadeA + atividadeB + atividadeA
    print(f"Total {total}")
