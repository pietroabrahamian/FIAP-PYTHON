# Peça para o usuário informar por input uma opção dentre as seguites: a, b, ou c.

# Se a opção for "a", imprima uma mensagem "bom dia"
# Se a opção for "b", imprima uma mensagem "boa tarde"
# Se a opção for "c", imprima uma mensagem "boa noite"
# Se for qualquer outra opção, imprima "opção inválida"

msn = input("Escolha uma opção entre: a, b c\n")
if msn == "a" or msn == "A":
    print("Bom dia")
else: 
    if msn == "b" or msn == "B":
        print("Boa tarde")
    else:
        print("Boa noite")

if msn == "a" or msn == "A":
    print("Bom dia")
elif msn == "b" or msn == "B":
    print("Boa tarde")
elif msn == "c" or msn == "C":
    print("Boa noite")
else:
    print("Valor inserido é inválido.")