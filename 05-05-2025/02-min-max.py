exemplo = [4, 1, 9, 2, 5, 3, 7, 10, 6, 8]

minimo = exemplo[0]

for valor in exemplo:
    if valor < minimo:
        minimo = valor
print(exemplo)
print("Valor Mínimo: ", minimo) 

maximo = exemplo[0]
for valor in exemplo:
    if valor > maximo:
        maximo = valor
print("Valor Máximo: ", maximo)



# print("Menor elemento da lista", min(exemplo))
# print("Maior elemento da lista", max(exemplo))