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
            operador = input('Insira o operador entre (+ - / *) qualquer outro valor resultará em média: ')
            if operador == "+" or operador == "soma":
                operacao = soma(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "-" or operador == "subtração":
                operacao = subtracao(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "*" or operador == "multiplicação":
                operacao = multiplicacao(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "/" or operador == "divisão":
                operacao = divisao(n1, n2)
                print(f"\n>>> Resultado: {operacao}\n")
            elif operador == "²" or operador == "quadrado":
                operacao = aoQuadrado(n1)
                print("\n>>> Primeiro Valor: {:.2f} \n".format(operacao))
                operacao = aoQuadrado(n2)
                print("\n>>> Segundo Valor: {:.2f} \n".format(operacao))
            elif operador == "**" or operador == "raiz":
                operacao = raiz(n1)
                print("\n>>> Primeiro Valor: {:.2f} \n".format(operacao))
                operacao = raiz(n2)
                print("\n>>> Segundo Valor: {:.2f} \n".format(operacao))
            else:
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