'''

Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:

Quais itens apareceram nas duas listas

Quais foram exclusivos de Laura

Quais foram exclusivos da Ana

Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

Exemplo de entrada:


Lista de Laura: leite, pão, café, açúcar 

Lista de Ana: pão, café, biscoito, chocolate 
Copiar código
Saída esperada:


Itens em ambas as listas: pão, café 

Itens exclusivos de Laura: leite, açúcar 

Itens exclusivos de Ana: biscoito, chocolate 
'''

lista1 = set(input('Lista de Laura: ').split(", "))

lista2= set(input('Lista de Ana: ').split(", "))

intersec = lista1.intersection(lista2)
print(f"Itens em ambas as listas: {intersec} ")

exclusivo_laura = lista1.difference(lista2)
print(f"Itens exclusivos de Laura: {exclusivo_laura}")

exclusivo_ana = lista2.difference(lista1)
print(f"Itens exclusivos de Ana: {exclusivo_ana}")