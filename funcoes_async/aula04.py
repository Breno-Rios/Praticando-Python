'''
Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários.
 No entanto, algumas notificações só devem ser enviadas se o usuário tiver ativado essa opção no sistema.
   Além disso, se o usuário for VIP, ele deve receber uma notificação prioritária antes das demais.

Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. Cada usuário tem um status diferente:

Ana: VIP (deve receber uma notificação prioritária antes das normais).
João: Usuário comum, mas ativou as notificações.
Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.

Saída esperada:

Enviando notificações...
Notificação VIP para Ana enviada!
Notificação normal para João enviada!
Carla desativou as notificações. Nada foi enviado.
Todas as notificações foram processadas!
'''

import asyncio

usuarios = [
    {"nome": "Ana", "vip": True, "notificacoes_ativadas": True},
    {"nome": "João", "vip": False, "notificacoes_ativadas": True},
    {"nome": "Carla", "vip": False, "notificacoes_ativadas": False},
]


async def notificar(usuario):
  if not usuario['notificacoes_ativadas']:
    print(f'{usuario['nome']} desativou as notificações. Nada foi enviado.')
    return
  
  if usuario['vip']:
    print(f'Notificação VIP para {usuario['nome']} enviada!')
    return
  
  if not usuario['vip']:
    print(f'NNotificação normal para {usuario['nome']} enviada!')
    return

async def main():
  print('Enviando notificações...')
  notificacoes = [asyncio.create_task(notificar(usuario)) for usuario in usuarios]
  await asyncio.gather(*notificacoes)
  print('Todas as notificações foram processadas!')


asyncio.run(main())