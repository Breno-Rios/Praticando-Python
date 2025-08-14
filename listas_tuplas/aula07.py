'''
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes.
 Mas, um erro foi identificado: um dos nomes está incorreto. 
 O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

Exemplo de Entrada:

Digite o nome incorreto: Carlos
Digite o nome correto: João
Copiar código
Saída esperada:

O nome Carlos foi substituído por João.
Lista atualizada: ['Ana', 'João', 'Pedro']
'''

lista = ['Ana', 'Carlos', 'Pedro']

substituir = input('Digite o nome incorreto: ')
nome = input('Digite o nome correto: ')

posicao = lista.index(substituir)
lista.remove(substituir)
lista.insert(posicao,nome)
  

print(f'O nome {substituir} foi substituído por {nome}. \n {lista}')

