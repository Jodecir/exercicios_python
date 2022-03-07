def pulaLinha():
    print("---------------------")

def desconto(a, b):
    return a * b / 100

fechado = False

while fechado == False:
    try:
        cliente = str(input("Insira o nome: ").capitalize())
        idade = int(input("Insira a idade: "))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        valorCurso = 0
        greeting = "Olá"

        print("\n>>> 1 - TI")
        print(">>> 2 - Psicologia")
        print(">>> 3 - Pacote Office")
        print(">>> 4 - Manicure")
        print(">>> 5 - Fotografia\n")
        
        try:
            curso = int(input("Digite o número: "))
        except FloatingPointError:
            print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
        except ValueError:
            print("Valor inválido. Deve-se digitar apenas números.")
        else:
            cursoMin = 1
            cursoMax = 5
            
            while curso > cursoMax or curso < cursoMin:
                curso = int(input('O número do curso está incorreto, Escolha entre 1 a 5:'))
            if curso == 1:
                valorCurso = 400
                pulaLinha()
                valorFinal = valorCurso - desconto(valorCurso, idade)
                print('{} {}, o curso desejado de R${} se torna R${} com o desconto da sua idade, que é {}%'.format(greeting, cliente, valorCurso, int(valorFinal), idade))
            elif curso == 2:
                valorCurso = 1200
                pulaLinha()
                valorFinal = valorCurso - desconto(valorCurso, idade)
                print('{} {}, o curso desejado de R${} se torna R${} com o desconto da sua idade, que é {}%'.format(greeting, cliente, valorCurso, int(valorFinal), idade))
            elif curso == 3:
                valorCurso = 100
                pulaLinha()
                valorFinal = valorCurso - desconto(valorCurso, idade)
                print('{} {}, o curso desejado de R${} se torna R${} com o desconto da sua idade, que é {}%'.format(greeting, cliente, valorCurso, int(valorFinal), idade))
            elif curso == 4:
                valorCurso = 149
                pulaLinha()
                valorFinal = valorCurso - desconto(valorCurso, idade)
                print('{} {}, o curso desejado de R${} se torna R${} com o desconto da sua idade, que é {}%'.format(greeting, cliente, valorCurso, int(valorFinal), idade))
            elif curso == 5:
                valorCurso = 300
                pulaLinha()
                valorFinal = valorCurso - desconto(valorCurso, idade)
                print('{} {}, o curso desejado de R${} se torna R${} com o desconto da sua idade, que é {}%'.format(greeting, cliente, valorCurso, int(valorFinal), idade))
            else:
                break
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True