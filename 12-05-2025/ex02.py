def maior_valor(v1, v2, v3):
    if v1 > v2 and v1 > v3:
        return v1
    elif v2 > v1 and v2 > v3:
        return v3
    else:
        return v3
x = int(input("Insira o primeiro valor: "))
y = int(input("Insira o segundo valor: "))
z = int(input("Insira o terceiro valor: "))

print(f"O maior valor entre {x}, {y} {z} é: {maior_valor(x,y,z)}")