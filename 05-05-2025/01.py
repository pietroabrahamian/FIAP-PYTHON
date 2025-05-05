compras = []

em_execução = True
while em_execução:
    print("Seja muito bem vindo a sua lista de compras")
    while em_execução:
        inserir_lista = input("Deseja inserir itens a sua lista de compra? (S/N)")
        if inserir_lista == "S" or inserir_lista == "s":
            item = input("Insira o seu produto: \n")
            compras.append(item)
        elif inserir_lista == "N" or inserir_lista == "n":
            print("O programa está sendo finalizado")
            em_execução = False
        else:
            print("Valor inserido inválido.")
print(*compras)