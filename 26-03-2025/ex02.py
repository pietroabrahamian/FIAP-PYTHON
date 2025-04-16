f = float(input("Qual a temperatura atual em Fahrenheit?"))
c = (f-32)/1.8

if c > 25:
    print("Está calor")

print(f"Está dtemperatura equivale a: {c:.2f}°C")