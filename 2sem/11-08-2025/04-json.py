import json

def main():
    with open("paciente.json") as arquivo:
        paciente = json.load(arquivo)

        print(paciente)

main()

