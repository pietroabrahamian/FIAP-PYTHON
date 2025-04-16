# (a) Pergunte a temperatura em Fahrenheit;
# Mostre o valor da temperatura em Celsius

F = float(input("Qual é a temperatura atual em Fahrenheit?"))
C = (F - 32)*5/9
print(f"A temperatura atual em C° é: C°{C:.2f}")

# (b) Pergunte a temperatura em Celsius;
# Mostre o valor a temperatura em Fahrenheit.
cel = float(input("Qual a temperatura atual em Celsius?"))
fah = (cel*9/5) + 32
print(f"A temperatura atual e Fahrenheit é:{fah:.2f}")