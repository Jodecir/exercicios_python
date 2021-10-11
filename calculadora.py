fechado = False

while fechado == False:
    try:
        n1 = abs(int(input('Insira o primeiro valor: ')))
        n2 = abs(int(input('Insira o segundo valor: ')))
        operador = input('Insira o operador entre (+-/*) qualquer outro valor resultará em média: ')
        media = int((n1 + n2) / 2)
        if operador == "+":
            operacao = n1 + n2
        elif operador == "-":
            operacao = n1 - n2
        elif operador == "*":
            operacao = n1 * n2
        elif operador == "/":
            operacao = n1 / n2
    except ZeroDivisionError:
        print("Não é possível realizar divisão por 0.")
    except ArithmeticError:
        print("Houve um erro ao realizar uma operação aritmética.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        print("\nResultado:", operacao,"\n")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True