from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entra 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('\033[36mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
