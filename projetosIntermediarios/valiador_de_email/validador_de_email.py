import re
import datetime
import random
from tokenize import group

#variaveis
email = ['deeppurple23@hearourvoicetee.com', 'heyhmm@freeallapp.com', 'redovoj@kwontol.com','rocko400@kimsangun.com', 'divsmc@itsmegru.com']
# email = ['texto.texxto']

# funcao principal
def verificar_email(e):
    position = random.randint(0, len(e) - 1)
    print(position)
    email_selecionado = e[position]
    print(f'original: {email_selecionado}')
    padrao = r'\w.*@\w*.com'
    verificador = (re.findall(padrao, email_selecionado))
    if verificador:
        print(f'verificador {verificador}')
        print('o email poderá ser utilizado como válido')
    return


if __name__ == '__main__':
    verificar_email(email)

