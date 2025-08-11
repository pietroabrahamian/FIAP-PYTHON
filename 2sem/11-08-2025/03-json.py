import json

def le_dados_paciente():
    paciente = {}
    paciente['nome'] = input("Qual o nome do paciente?")
    paciente['idade'] = int(input("Qual a idade do paciente?"))
    paciente['queixa'] = input("Qual a queixa do paciennte?")
    return paciente

def main():
    paciente = le_dados_paciente()
    print(f"O paciente lido foi: {paciente}")
    with open ('paciente.json', "w") as arquivo:
        json.dump(paciente, arquivo, indent=4 )

main()
