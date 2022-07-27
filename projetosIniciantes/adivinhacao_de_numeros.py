import random
from re import S

def modulo_do_jogo():
    number_to_be_found = random.randrange(0,15,1)
    primeira_tentativa = int(input('chute um número entre 0 e 15: '))
    tentativas_restantes = 3
    while tentativas_restantes > 0:
        if (primeira_tentativa == number_to_be_found):
            print('voce acertou! ')
            print('sobraram: ', tentativas_restantes + 1, " tentativas_restantes")
            break
        if tentativas_restantes == 1:
            jogar_novamente = input('deseja jogar novamente?(s/n) ')
            if jogar_novamente == 's':
                return modulo_do_jogo
            elif jogar_novamente == 'n':
                print('adeus mundo!! _-_')
                return
            else:
                print('digite s ou n: ')
                return guessingNumber()
        hint = int(number_to_be_found - primeira_tentativa)
        tentativas_restantes -= 1
        print('voce possui ', tentativas_restantes + 1, " tentativas")
        print('a diferenca entre seu chute e a resposta e: ', hint)
        primeira_tentativa = int(input('tente novamente: '))


def guessingNumber():
    deseja_jogar = input('deseja jogar?(s/n)')
    if deseja_jogar == 's':
            modulo_do_jogo()
    else:
        return
        






if __name__ == '__main__':
    guessingNumber()