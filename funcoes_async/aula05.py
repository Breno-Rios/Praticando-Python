'''
Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. O sistema deve seguir a seguinte lógica:

Primeiro, verificar se o pagamento foi aprovado;
Se o pagamento for aprovado, verificar se há estoque disponível;
Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.
A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. Confira o código:

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]
Copiar código
O programa deve simular essa lógica para três pedidos, exibindo mensagens conforme o processamento ocorre.

Saída esperada:

Processando pedido #101...
Pagamento aprovado para pedido #101.
Estoque disponível para pedido #101.
Pedido #101 confirmado! Enviado para entrega.
 
Processando pedido #102...
Pagamento aprovado para pedido #102.
Estoque indisponível para pedido #102. Pedido cancelado.
 
Processando pedido #103...
Pagamento recusado para pedido #103. Pedido cancelado.
 
Todos os pedidos foram processados!
'''
import asyncio

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def processar_pedidos(pedido):
  print(f'Processando pedido {pedido['id']}...')
  if pedido['pagamento_aprovado']:
    print(f'Pagamento aprovado para pedido {pedido['id']}.')
    if pedido['estoque_disponivel']:
      print(f'Estoque disponível para pedido {pedido['id']}.')
      print(f'Pedido {pedido['id']} confirmado! Enviado para entrega. \n')
      return
    else:
      print(f'Estoque indisponível para pedido {pedido['id']}. Pedido cancelado.\n')
      return
  else:
    print('Pagamento recusado para pedido #103. Pedido cancelado.\n')
    return

async def main():
  tarefa = [asyncio.create_task(processar_pedidos(p)) for p in pedidos]
  await asyncio.gather(*tarefa)

  print('Todos os pedidos foram processados!')

asyncio.run(main())


''' SUGESTÃO DO INSTRUTOR'''

'''
import asyncio

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def verificar_pagamento(pedido):
    await asyncio.sleep(1)
    if pedido["pagamento_aprovado"]:
        print(f"Pagamento aprovado para pedido #{pedido['id']}.\n")
        return True
    else:
        print(f"Pagamento recusado para pedido #{pedido['id']}. Pedido cancelado.\n")
        return False

async def verificar_estoque(pedido):
    await asyncio.sleep(1)
    if pedido["estoque_disponivel"]:
        print(f"Estoque disponível para pedido #{pedido['id']}.\n")
        return True
    else:
        print(f"Estoque indisponível para pedido #{pedido['id']}. Pedido cancelado.\n")
        return False

async def processar_pedido(pedido):
    print(f"Processando pedido #{pedido['id']}...\n")
    
    pagamento_ok = await verificar_pagamento(pedido)
    if not pagamento_ok:
        return
    estoque_ok = await verificar_estoque(pedido)
    if not estoque_ok:
        return
    print(f"Pedido #{pedido['id']} confirmado! Enviado para entrega.\n")

async def main():
    for pedido in pedidos: 
        await processar_pedido(pedido)
    print("\nTodos os pedidos foram processados!\n")

asyncio.run(main())

'''

