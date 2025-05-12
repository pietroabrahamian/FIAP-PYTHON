from datetime import datetime

def cumprimenta(nome):
    agora = datetime.now()
    hora = agora.hour
    if 5 <= hora < 12:
        message = f"Bom dia, {nome}"
        print(message)
    else:
        message = f"Boa noite, {nome}"
        print(message)

nome = input("Qual o seu nome?\n")
cumprimenta(nome)