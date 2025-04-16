# pergunte ao usuário qual o seu saldo no banco
# mostre mensagens diferente se o saldo for maior ou menor do que zero 

saldo = float(input("Qual seu saldo no banco?"))

if saldo > 0:
    print("Parabéns seu saldo está positivo! Continue assim!!")
else:
    print("Eita! Seu saldo está negativo. Organize suas finanças para melhorar a sua conta!")