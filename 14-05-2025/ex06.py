from math import pi

def area_circulo(raio):
    area = pi*(raio**2)
    return area

raios = [0.5, 3.0, 1.0, 5.4, 8.0, 12.3, 2.7]
conta = 0
for raio in raios:
    area = area_circulo(raio)
    if area > 20.0:
        print(raio)
        conta = conta + 1

print(conta)