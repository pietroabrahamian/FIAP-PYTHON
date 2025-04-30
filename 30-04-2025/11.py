compras = []

# numero_itens = int(input("Quantos itens você deseja colocar na lista de compras?"))
# itens_inseridos = 0

# while itens_inseridos < numero_itens:
#     item = input("Digite um item:")
#     compras.append(item)
#     itens_inseridos += 1
# print(f"Lista cirada: \n {compras}")
simnao = input("Deseja inserir itens a sua lista? (S/N)")

while simnao == "S" or simnao == "s":
    item = input("Digite o item:")
    compras.append(item)
    while True: 
        simnao = input("Deseja inserir mais um item? (S/N)")
 
        if simnao == "S" or simnao == "s":
            break
        elif simnao == "N" or simnao == "n":
            print("Itens adicionados a sua lista.")
            break
        else:
            print("Valor não compreendido. Digite novamente")

print(f"Lista finalizada: \n{compras}")

