'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. 
Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.


'''

temperatura= float(input("Digite a temperatura atual: "))

if(temperatura>25):
    print('Alerta! temperatura acima do limite permitido')
else:
    print('Temperatura dentro do limite.')