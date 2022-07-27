import webbrowser
from time import strftime
import time
from playsound import playsound
import os
import datetime

def alarmYT(hora_desejada, minuto_desejado):
    while True:
        hora_local = strftime('%H')
        minuto_local = strftime('%M')
        time.sleep(5)
        print(hora_local, minuto_local)
        if (hora_local == hora_desejada) and (minuto_local == minuto_desejado) :
            print(hora_local, minuto_local, 'horario marcado!!')
            webbrowser.open('https://www.youtube.com/watch?v=60ItHLz5WEA')
            return False

def temporizador(horas, minutos, segundos):
    horas = int(horas)
    minutos = int(minutos)
    segundos = int(segundos)
    tempo_total_segundos = horas * 3600 + minutos * 60 + segundos 
    while True:
        tempo = datetime.timedelta(seconds = tempo_total_segundos)
        tempo_total_segundos -= 1
        time.sleep(1)
        print(tempo)
        if tempo_total_segundos < 0:
            print('acabou o tempo!! tocarei uma musica caso voce tenha a bilioteca do pip playsound \O/ para sair deve fechar o prompt ')
            playsound(os.getcwd() +'\projetosIniciantes\\arquivos_necessarios\musica.mp3')
            return False
    



def clockWork():
    funcao = int(input('deseja um alarm(0) ou um temporizador(1): '))
    if funcao == 0:
        hora_desejada = input('digite a hora desejada: ')
        minuto_desejado = input("digite o minuto desejado: ")
        alarmYT(hora_desejada, minuto_desejado)
    if funcao == 1:
        horas = input('digite quantas horas de espera: ')
        minutos = input('digite quantos minutos de espera: ')
        segundos = input('quantos segundos de espera: ')
        temporizador(horas, minutos, segundos)
    reiniciar = input('deseja reinicar o relogio?(s/n) ')


if __name__ == '__main__':
    clockWork()
