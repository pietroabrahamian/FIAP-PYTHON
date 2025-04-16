print("Preciso que me de a nota das suas 3 atividaes:")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1+n2+n3)/3

if media >= 6:
    print("Aprovado!!")
else:
    print("Fará a recuperação.")