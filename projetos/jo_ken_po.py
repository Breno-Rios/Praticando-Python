'''
Lucas quer criar um jogo de pedra, papel e tesoura para jogar contra o computador. 
Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura.
 O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

Pedra ganha de Tesoura (Pedra quebra Tesoura);
Tesoura ganha de Papel (Tesoura corta Papel);
Papel ganha de Pedra (Papel cobre Pedra);
Se ambos escolherem a mesma opção, é um empate.
Exemplo de entrada:

Escolha: pedra, papel ou tesoura? papel  
Copiar código
Saída esperada:

Computador escolheu: pedra
Você venceu!  
Copiar código
Caso o computador vença:

Computador escolheu: tesoura  
Você perdeu!  
Copiar código
Caso o computador escolha a mesma opção que você:

Computador escolheu: papel 
Empate!
'''
import random
import asyncio

async def jogo(game1, game2):
    if game1 == game2:
        return f"Computador escolheu: {game2}\nEmpate!"

    if game1 == "Pedra":
        if game2 == "Tesoura":
            return f"Computador escolheu: {game2}\nVocê venceu!"
        else:  # game2 == "Papel"
            return f"Computador escolheu: {game2}\nVocê perdeu!"

    elif game1 == "Papel":
        if game2 == "Pedra":
            return f"Computador escolheu: {game2}\nVocê venceu!"
        else:  # game2 == "Tesoura"
            return f"Computador escolheu: {game2}\nVocê perdeu!"

    elif game1 == "Tesoura":
        if game2 == "Papel":
            return f"Computador escolheu: {game2}\nVocê venceu!"
        else:  # game2 == "Pedra"
            return f"Computador escolheu: {game2}\nVocê perdeu!"

    
async def main():
  game1 = input('Escolha: pedra, papel ou tesoura? ')
  game2 = random.choice(['Pedra','Papel','Tesoura'])
  resultado= await jogo(game1,game2)
  print(resultado)
  

asyncio.run(main())