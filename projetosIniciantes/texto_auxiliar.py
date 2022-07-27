from cgi import print_directory
import math
import re
import datetime
import webbrowser
import time 
from time import strftime
import os
from playsound import playsound

# # padrao = r"^\d*\s+"
# # padrao2 = r"\s+\d*$"
# # texto = '25 gas+gdsa 43'
# # regex = re.findall(padrao, texto)
# # regex2 = re.findall(padrao2, texto)
# # convert = list(map(int, regex))
# # convert2 = list(map(int, regex2))
# # # sum = list(map(sum, convert, convert2))
# # print(convert, convert2)
# # soma = convert + convert2
# # print(math.prod(soma))
# # sinal = r"\+"
# # regex3 = re.findall(sinal, texto)
# # print(regex3)

# # def padrao_sinal(texto):
# #     padrao_sinal = r"[\+|\-|\*|\/]"
# #     regex_sinal = re.findall(padrao_sinal, texto)
# #     string = "".join(regex_sinal)
# #     return string

# # print(padrao_sinal('/'))


# # padrao0 = r"\s*\d+$"
# # padrao1 = r"^\d+\s*"
# # regex0 = re.findall(padrao1, '6531 *8')
# # print(list(map(int, regex0)))

# lista = [36]
# lista2 = [54]
# s = [str(integer) for integer in lista]
# a_string = "".join(s)
# res = int(a_string)

# print(type(res))


# def alarmYT():
#     # # return print(strftime("%I:%M"))
#     horario = strftime('%I:%M')
#     while True:
#         horario = strftime('%I:%M')
#         time.sleep(5)
#         print(horario)
#         if horario == "04:":
#             webbrowser.open('https://www.youtube.com/watch?v=60ItHLz5WEA')
#             return False



# if __name__ == '__main__':
#     alarmYT()

# def temporizador():
#     segundos = 10
#     while True:
#         tempo = datetime.timedelta(seconds = segundos)
#         segundos -= 1
#         time.sleep(1)
#         print(tempo)
#         if segundos == 0:
#             print('acabou o tempo!! tocarei uma musica \O/')
#             playsound(os.getcwd() +'\projetosIniciantes\musica.mp3')
#             return False

# if __name__ == '__main__':
#     temporizador()

# directory = os.getcwd()
# print_directory()

# playsound(os.getcwd() + '\projetosIniciantes\musica.mp3')
# C:\Users\vicas\projetosInteressantes\projetosIniciantes

# texto = 'teXto'
# regex_teste = re.search(r'(?i)xt', texto).group()
# print(regex_teste)

# def padrao_sinal(texto):
#     padrao_sinal = r"[\+|\-|\*|\/|\*\*|sqrt|x|X]"
#     regex_sinal = re.findall(padrao_sinal, texto)
#     string = "".join(regex_sinal)
#     return string

# print(padrao_sinal('x'))

# def calculo():
#     texto = '25 x 25'
#     padrao_num0 = r"^\d+\s*"
#     padrao_num1 = r"\s*\d+$"
#     regex0 = re.findall(padrao_num0, texto)
#     regex1 = re.findall(padrao_num1, texto)
#     lista_str0 = [str(integer) for integer in regex0]
#     lista_str1 = [str(integer) for integer in regex1]
#     str0 = "".join(lista_str0)
#     str1 = "".join(lista_str1)
#     convert0 = int(str0)
#     if regex1:
#         convert1 = int(str1)
#     sinal = 'x'
#     if sinal == '*' or sinal == 'x':
#         resultado = convert0 * convert1
#         return resultado
#     elif sinal == '/':
#         resultado = convert0 / convert1
#         return resultado
#     elif sinal == '-':
#         resultado = convert0 - convert1
#         return resultado
#     elif sinal == "+":
#         resultado = convert0 + convert1
#         return resultado
#     elif sinal == '**':
#         resultado = math.pow(convert0, convert1)
#         return resultado
#     elif sinal == 'sqrt':
#         resultado = math.sqrt(convert0)
#         return resultado
#     else:
#         return 'valor nao encontrado'

# print(calculo())

# matcher = re.match(r'tex', 'texto').group()
# print(type(matcher))


# def padrao_sinal(texto):
#     padrao_sinal = r"[\+|\-|\*|\/|\*\*|sqrt|x|X]"
#     regex_sinal = re.search(padrao_sinal, texto).group()
#     return regex_sinal

# print(padrao_sinal('432 +'))

# \s*\+|\-|\*|\/|\*\*|sqrt|x|X\s*\d*
# regex1 = re.search(r'\s+\d+$', '532 x')
# print(regex1)
# print(regex1)

# primeira_tentativa = input('chute um número entre 0 e 15: ')
# primeira_tentativa = '35dgdsagsa'
# capturando_numeros = re.search(r"\d*", primeira_tentativa)
# # if capturando_numeros:
# #     capturando_numeros = int(capturando_numeros.group())
# print(type(capturando_numeros.group()))
# print(capturando_numeros.group())
