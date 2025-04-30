# Exercicio: modifique o programa para qeu, se o usuario digitar inicio mairo do que fim, seja mostrado o interbalo decrescente

inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

passo = 1
if inicio < fim:
    passo = -1

for numero in range (inicio, fim, passo):
    print(numero)