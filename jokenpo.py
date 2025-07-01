from random import randint #para importar a função de randomizar
from time import sleep # para importar a função de espera
itens = ('Pedra','Papel','Tesoura') #atribuindo itens do pedra, papel e tesoura
computador = randint(0,2) # randomizando a escolha do computador
escolha=int(input('escolha sua opção no Pedra, Papel e Tesoura: \n0 - Pedra\n1 - Papel\n2 - Tesoura\n:')) # opções de interface do usuario
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('verificando resultado')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)
print('.')
sleep(0.5)

if computador == 0:
    if escolha ==0:
        print('vocês empataram pois ambos escolheram {}'.format(itens[escolha]))
    elif escolha==1:
        print('você ganhou pois {} ganha de {} que foi a escolha do computador'.format(itens[escolha],itens[computador]))
    elif escolha==2:
        print('você perdeu pois {} perde para {} que foi a escolha do computador'.format(itens[escolha],itens[computador]))
    else:
        print('ERROR!! OPÇÃO INVALIDA!!\nescolha apenas as opções Validas de 0 a 2! ')
elif computador == 1:
    if escolha == 0:
        print('você perdeu pois {} perde para {} que foi a escolha do computador'.format(itens[escolha], itens[computador]))
    elif escolha == 1:
        print('vocês empataram pois ambos escolheram {}'.format(itens[escolha]))
    elif escolha == 2:
        print('você ganhou pois {} ganha de {} que foi a escolha do computador'.format(itens[escolha],itens[computador]))
    else:
        print('ERROR!! OPÇÃO INVALIDA!!\nescolha apenas as opções Validas de 0 a 2! ')
elif computador == 2:
    if escolha == 0:
        print('você ganhou pois {} ganha de {} que foi a escolha do computador'.format(itens[escolha], itens[computador]))
    elif escolha == 1:
        print(
            'você perdeu pois {} perde para {} que foi a escolha do computador'.format(itens[escolha], itens[computador]))
    elif escolha == 2:
        print('vocês empataram pois ambos escolheram {}'.format(itens[escolha]))
    else:
        print('ERROR!! OPÇÃO INVALIDA!!\nescolha apenas as opções Validas de 0 a 2! ')
