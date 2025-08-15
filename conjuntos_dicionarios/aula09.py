'''
Laura está organizando um workshop sobre tecnologia e precisa de um programa que permita remover participantes que desistiram do evento.
 O sistema armazena os participantes em um dicionário, onde cada chave é o nome e o valor é um conjunto com os dados do participante.
   O programa deve solicitar o nome de um participante e remover esse nome da lista de participantes registrados, caso exista.

Exemplo de entrada:


participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 
Copiar código

Nome do participante a ser removido: Carla 
Copiar código
Saída esperada:


Lista atualizada de participantes: 

Workshop 1: {'Alice', 'Bruno', 'Diego'} 

Workshop 2: {'Fernanda', 'Gustavo', 'Helena'} 
'''

participantes = { 

    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"}, 

    "Workshop 2": {"Fernanda", "Gustavo", "Helena"} 

} 

remover = input('Nome do participante a ser removido: ')

for item in participantes.keys():
  if remover in participantes[item]:
    participantes[item].remove(remover)

print('Lista atualizada de participantes: ')
for i in participantes.items():
  print(i)