# (a) Peça ao usuário que informe comprimento e largura de um terreno retangular.
print("Preciso que vc me informe o comprimento e a largura do seu terreno.")
comprimento = float(input("Comprimento ="))
largura = float(input("Largura ="))
area = comprimento*largura 
print(f"A área do seu terreno é de:{area}")

# (b) Peça ao usuário que informe o preço total do terreno.
# Calcule e mostre qual o preço por metro quadrado.
preco = float(input("Qual o valor total do terreno?"))
preco_m = preco/area
print(f"O valor do seu terreno por metro quadrao é de: {preco_m}")