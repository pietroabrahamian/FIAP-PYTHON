# Exercício "DOAÇÃO DE SANGUE", parte 1. Pergunte a idade da pessoa. (Teremos outras versões desse exercício, levando em conta mais requisitos para doar sangue.)

# Se a idade estiver no intervalo de 18 a 60 anos, diga "Pode doar sangue!"
# Se a idade for menor de 18, mas pelo menos 16, pergunte se tem autorização dos pais. (Pode instruir a pessoa a digitar S ou N, por exemplo.) Imprima mensagens diferentes dependendo da resposta.

idade = int(input("Qual a sua idade?"))

if 18 <= idade <= 60:
    print("Pode doar sangue!")
if 18 > idade >= 16:
    autorizacao = input("Você possui autorização dos responsáveis para doação de sangue? (S/N)")
    if autorizacao == "s" or autorizacao == "S":
        print("Você pode doar sangue!")
    else:
        print("Você não pode doar sangue.")
    