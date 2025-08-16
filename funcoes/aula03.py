'''
Beatriz está desenvolvendo um sistema de atendimento para um site de serviços.
Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. 
O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";

Entre 12h e 18h, exibir "Boa tarde";

Após 18h, exibir "Boa noite".

Exemplo de entrada:


Digite a hora atual (0-23): 15 
Copiar código
Saída esperada:


Boa tarde!
'''

def saudacao(hora):
  if hora > 18:
    return print('Bom noite!')
  elif hora > 12:
    return print('Boa tarde!')
  else:
    print('Bom dia!')

hora = int(input('Digite a hora atual (0-23): '))
saudacao(hora)