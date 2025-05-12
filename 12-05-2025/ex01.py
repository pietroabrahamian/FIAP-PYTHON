def menor_valor(v1, v2):
    if v1 > v2:
        return v2
    else:
        return v1
    
x = int(input("Insira o primeiro valor"))
y = int(input("Insira o segundo valor"))

print(f"O menor valor entre {x} e {y} é: {menor_valor(x,y)}")