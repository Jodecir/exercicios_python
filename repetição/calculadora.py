def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def media(a, b):
    return (a + b) / 2

def aoQuadrado (a):
    return a ** 2

def raiz (a):
    return a ** (1/2)

fechado = False

while fechado == False:
    try:
        n1 = abs(int(input('Insira o primeiro valor: ')))
        n2 = abs(int(input('Insira o segundo valor: ')))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        try:
            print(">> [1]: Soma")
            print(">> [2]: Subtracão")
            print(">> [3]: Multiplicacão")
            print(">> [4]: Divisão")
            print(">> [5]: ²")
            print(">> [6]: Raiz Quadrada")
            print(">> [7]: Média")

            operador = input('Insira o número da operação: ')
            if operador == "1" or operador == "+" or operador == "soma":
                operacao = soma(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "2" or operador == "-" or operador == "subtração":
                operacao = subtracao(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "3" or operador == "*" or operador == "multiplicação":
                operacao = multiplicacao(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "4" or operador == "/" or operador == "divisão":
                operacao = divisao(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "5" or operador == "²" or operador == "quadrado":
                operacao = aoQuadrado(n1)
                print("\n>>> Primeiro Valor: {:.2f} \n".format(operacao))
                operacao = aoQuadrado(n2)
                print("\n>>> Segundo Valor: {:.2f} \n".format(operacao))
            elif operador == "6" or operador == "**" or operador == "raiz":
                operacao = raiz(n1)
                print("\n>>> Primeiro Valor: {:.2f} \n".format(operacao))
                operacao = raiz(n2)
                print("\n>>> Segundo Valor: {:.2f} \n".format(operacao))
            elif operador == "7" or operador == "**" or operador == "media":
                operacao = int(media(n1, n2))
                print(f"\n>>> Resultado: {operacao}\n")
        except ZeroDivisionError:
            print("Não é possível realizar divisão por 0.")
        except ArithmeticError:
            print("Houve um erro ao realizar uma operação aritmética.")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True