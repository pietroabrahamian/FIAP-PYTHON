paciente = {}

paciente['nome'] = input("Qual o nome do paciente?")
paciente['idade'] = int(input("Qual a idade do paciente?"))
paciente['queixa'] = input("Qual a queixa do paciennte?")

status = "continue"
while status == "continue":
    opcao = int(input("Menu: \n 1. Add paciente \n 2. Encerrar o programa \n"))
    if opcao == 1:
        paciente['nome'] = input("Qual o nome do paciente?")
        paciente['idade'] = int(input("Qual a idade do paciente?"))
        paciente['queixa'] = input("Qual a queixa do paciennte?")
    else:
        print("Obrigado por fazer parte disso! \n Volte sempre!!")
        break

for pessoa in paciente:
    print(f"{pessoa}: {paciente[pessoa]}")