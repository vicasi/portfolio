import random

def rps(rodada, ganhos):
    escolha = input('pedra, papel e tesoura, escolha um(pe,pa,te) :)')
    escolha_maquina = random.randrange(0,2,1)
    def switcher(item):
        escolha = {
            'pe' : 0,
            'pa' : 1,
            'te' : 2  
        }
        return escolha.get(item, False)
    sua_escolha = switcher(escolha)
    if rodadas == 2:
        continuar = input('deseja continuar? (s/n)')
        if continuar == 's':
            pass
        else:
            return print(rodada, ganhos)
    rodadas(sua_escolha, escolha_maquina, rodada, ganhos)
    
def rodadas(sua_escolha, escolha_maquina, rodada, ganhos):
        if sua_escolha == escolha_maquina:
            ganhos += 1
            print('voce ganhou ', ganhos, ' rodadas contra a maquina')
            rodada += 1
            if rodada == 2:
                return(rodada, ganhos)
        else:
            print('lamento, nao foi dessa vez :(')
            rodada += 1
            if rodada == 2:
                return rps(rodada, ganhos)

def deseja_jogar():
    rodada = 0
    ganhos = 0
    deseja = input('deseja jogar? (s/n)')
    if deseja == 'n':  
        return print('bye bye world :(')
    while deseja == 's':
        rps(rodada, ganhos)
        deseja = input('deseja jogar novamente? (s/n)')
        if deseja == 'n':
            return print('bye bye world :(')
        









if __name__ == '__main__':
    deseja_jogar()