# Vamos usar esse exercício para aprender algumas operações de string. Peça um texto por input.

# (a) Mostre esse texto em MAIÚSCULAS (método upper());
frase = input("Escreva uma pequena frase")
print("Maiuscula", frase.upper())

# (b) Mostre esse texto trocando a letra 'a' por 'i' (método replace());
print(f"Trocando 'a' por 'i':{frase.replace('a', 'i')}")

# (c) Mostre o número de ocorrências da letra 'e'.
print(f"Existem {frase.count('e')} nesse texto")