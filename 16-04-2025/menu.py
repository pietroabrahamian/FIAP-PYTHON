em_execucao = True

# print("Olá seja muito bem vindo a sua calculadora!")
# while em_execucao:
#     print("Escolha uma opção:")
#     print("A - Soma")
#     print("B - Subtração")
#     print("C - Multiplicação")
#     print("D - Divisão")
#     print("E - Sair")
    
#     opcao = input()
#     if opcao == 'A':
#         print('Digite o primeiro valor para a soma:')
#         x = float(input())
#         print('Digite o segundo valor para a soma:')
#         y = float(input())
        
#         print('Resultado da soma:', x+y)
#     elif opcao == 'B':
#         print('Digite o primeiro valor para a subtração:')
#         x = float(input())
#         print('Digite o segundo valor para a subtração:')
#         y = float(input())
        
#         print('Resultado da subtração:', x-y)
#     elif opcao == 'C':
#         print('Digite o primeiro valor para a multiplicação:')
#         x = float(input())
#         print('Digite o segundo valor para a multiplicação:')
#         y = float(input())
        
#         print('Resultado da multiplicação:', x*y)
#     elif opcao == 'D':
#         print('Digite o primeiro valor para a divisão:')
#         x = float(input())
#         print('Digite o segundo valor para a divisão:')
#         y = float(input())
        
#         print('Resultado da divisão:', x/y)
#     else:
#         print("Certo! Estamos encerrando...")
#         em_execucao = False

#  TENTANDO DE OUTRO JEITO

print("Seja muito bem vindo a sua calculadora!")
while em_execucao:
    inicio = input("Deseja operar? S/N: ")

    if inicio == 'N' or inicio == 'n':
        print("Certo! Estamos encerrando...")
        em_execucao = False
    print("Ok!! Primeiro digite os valores que você quer operar:")
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))

    print("Agora escolha qual a sua operação:")
    print("A - Soma")
    print("B - Subtração")
    print("C - Multiplicação")
    print("D - Divisão")
    print("E - Sair")
    
    opcao = input()
    
    if opcao == 'A' or opcao == 'a':
        print('Resultado da soma:', n1+n2)
    elif opcao == 'B'or opcao == 'b':
        print('Resultado da subtração:', n1-n2)
    elif opcao == 'C'or opcao == 'c':
        print('Resultado da multiplicação:', n1*n2)
    elif opcao == 'D' or opcao == 'd':
        print('Resultado da divisão:', n1/n2)
    else:
        print("Certo! Estamos encerrando...")
        em_execucao = False
