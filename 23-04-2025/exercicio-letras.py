palavra = input("Digite uma palavra:")
i = 0
while i < len(palavra):
    if palavra[i] != "a":
        print(palavra[i])
    i += 1

n = 0
contagem = 0
while n < len(palavra):
    if palavra[n] == "e":
        contagem += 1
    n += 1

print(palavra.count("e")) #conta quantas letras "e" tem na palavra
print(f"A quantidade de letras 'e' na palavra '{palavra}' é: {contagem}")