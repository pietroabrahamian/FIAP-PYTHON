n = 1

while n <= 10: # inicialização while externo + condição n <= 10
    multi = 1
    print(f"Tabuada do {n}:")
    while multi <= 10: # inicialização while interno + condição multi <= 10
        print(f"{n} x {multi} = {n * multi}")
        multi += 1 # atualização do while interno

    print()
    n += 1 # atualização do while externo
