from re import I


def madLibGenerator():
    loop = 1
    while loop < 10:
        noun = input("escolha um nome: ")
        p_noun = input("escolha um nome plural: ")
        noun2 = input("escolha um outro nome: ")
        place = input("escolha um local: ")
        adjective = input("escolha um adjetivo: ")
        noun3 = input("mais uma vez, escolha um nome: ")
        print('-------------------------------------')
        print("seja legal com ",noun," principalmente com ", p_noun)
        print ("pois o ", noun, 'pode ser um ', noun2,",")
        print ("seja legal com seu",p_noun," em cima da ",place)
        print ("onde o clima sempre é ",adjective,".")
        print ()
        print ("voce pode achar que este é a ",noun3,",")
        print ("mas não é.")
        print ("------------------------------------------")
        playMore = input('deseja continuar? (s/n) ')
        if playMore == 's':
            loop = 1
        else:
            loop = 10

if __name__ == '__main__':
    madLibGenerator()
