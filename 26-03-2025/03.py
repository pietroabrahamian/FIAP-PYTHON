# ler dois numeros por input e oferecer duas opções distintas de operações
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

print("Qual a operação desejada? Digite o número correspodente.")
print("1. soma (x + y)")
print("2. potenciação (x elevado a y)")
opcao = int(input)

#Exercicio: mostrar resultado correspondente à operação desejada
if opcao == 1:
    print("A soma é: ", x+y)
else:
    print("A potenciação é: ", x**y)