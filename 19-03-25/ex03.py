# Calcular a distância de um ponto até a origem (coordenada (0, 0) do plano). Seu programa irá:

# Ler as coordenadas x e y de um ponto (leia uma de cada vez, isto é, use inputs separados para o x e o y);
# Calcular a distância de (x, y) até (0, 0), também chamado de "magnitude" desse ponto;
# Mostrar a distância.

x = int(input("Me de a cordenada de X"))
y = int(input("Me de a cordenada de Y"))
distancia = ((x**2)+(y**2))**1/2
print(f"A distância entre ({x},{y}) à (0,0) é: {distancia}")

# BÔNUS (a): calcular distância entre dois pontos distintos
x2 = int(input("Me de outro valor de X"))
y2 = int(input("Me de outro valor de Y"))
distancia2 = float(((x-x2)**2)+((y-y2)**2)**1/2)
print(f"A distância entre ({x},{y}) e ({x2},{y2}) é: {distancia2}")

# BÔNUS (b): calcular distância entre dois pontos em 3D (isto é, pontos com coordenadas (x, y, z))
z = int(input("Agora para calcular dois pontos em 3D, me de o valor de Z"))
distancia3 = float(((x**2)+(y**2)+(z**2))**1/2)
print(distancia3)