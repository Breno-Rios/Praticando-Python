'''

Rafaela trabalha na área de marketing e quer criar mensagens personalizadas para os clientes.
 Ela precisa de um programa que permita exibir saudações baseadas no nome do cliente e na cidade onde ele mora.

Crie um programa que solicite o nome e a cidade de um cliente e exiba uma mensagem de boas-vindas personalizada.

Exemplo de Entrada:

Digite o nome do cliente: Laura
Digite a cidade do cliente: Rio de Janeiro
Copiar código
Saída esperada:

Olá, Laura! Bem-vinda ao sistema da cidade de Rio de Janeiro.

'''

nome_cliente= input('Digite o nome do cliente: ')
nome_cidade= input('Digite o nome da cidade do cliente: ')

print(f'Olá, {nome_cliente}! Bem-vinda ao sistema da cidade de {nome_cidade}')