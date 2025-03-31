# Pergunte a nota de um aluno em três atividades diferentes. Calcule a média entre as três.
n1 = float(input("Qual a nota da primeira atividade?"))
n2 = float(input("Qual a nota da segunda atividade?"))
n3 = float(input("Qual a nota da terceira atividade?"))
if 0 > n1 or n2 or n3 > 10:
    print("Entrada inválida, pfv insira um valor entre 0 e 10.")
   
else:
    media = (n1 + n2 + n3)/3
    print(f"Sua média é: {media}")

    if media >= 6.0:
        print("Você foi aprovado!")
    else:
        print("Nota insuficiente para aprovação direta.")
        if media >= 3.0:
            print("Você está de recuperação")
        else:
            print("Você foi reprovado!")