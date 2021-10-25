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
            operador = input('Insira o operador entre (+-/*) qualquer outro valor resultará em média: ')
            if operador == "+" or operador == "soma":
                operacao = n1 + n2
                print("\n>>> Resultado:", operacao,"\n")
            elif operador == "-" or operador == "subtração":
                operacao = n1 - n2
                print("\n>>> Resultado:", operacao,"\n")
            elif operador == "*" or operador == "multiplicação":
                operacao = n1 * n2 
                print("\n>>> Resultado:", operacao,"\n")
            elif operador == "/" or operador == "divisão":
                operacao = n1 / n2
                print("\n>>> Resultado:", operacao,"\n")
            else:
                media = int((n1 + n2) / 2)
                operacao = media
                print("\n>>> Resultado da média:", operacao,"\n")
        except ZeroDivisionError:
            print("Não é possível realizar divisão por 0.")
        except ArithmeticError:
            print("Houve um erro ao realizar uma operação aritmética.")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True