import random

def diceRoll():
    while True:
        deseja_jogar = input('deseja jogar? (s/n): ')
        if deseja_jogar == 's':
            print(random.randint(1, 6))
        elif deseja_jogar == 'n':
            return print('bye bye world :/')
        else:
            print('precisa digitar exatamente \'s\' ou \'n\'')

if __name__ == '__main__':
    diceRoll()