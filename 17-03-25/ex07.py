#  Pergunte o ano em que o usuário nasceu.
ano = int(input("Em que ano você nasceu?"))
# (a) Calcule e informe sua idade
idade = 2025 - ano
if idade < 18:
    print("Para utilizar o sistema é necessária uma autorização dos responsáveis.")
else:
    print("Você possui idade suficiente para utilizar o sistema.")    