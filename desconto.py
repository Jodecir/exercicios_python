fechado = False

while fechado == False:
    cliente = str(input("Nome: "))
    idade = int(input("Idade: "))
    valorCurso = 0
    greeting = "Olá"

    curso = int(input(" \n 1-TI \n 2-Psicologia \n 3-Pacote Office \n 4-Manicure\n 5-Fotografia\n Digite o número:"))

    if curso == 1:
        valorCurso = 400
        desconto = valorCurso * idade / 100
        print(greeting,cliente,",","o curso desejado com desconto ficou: R$",valorCurso-desconto)
    elif curso == 2:
        valorCurso = 1200
        desconto = valorCurso * idade / 100
        print(greeting,cliente,",","o curso desejado com desconto ficou: R$",valorCurso-desconto)
    elif curso == 3:
        valorCurso = 100
        desconto = valorCurso * idade / 100
        print(greeting,cliente,",","o curso desejado com desconto ficou: R$",valorCurso-desconto)
    elif curso == 4:
        valorCurso = 149
        desconto = valorCurso * idade / 100
        print(greeting,cliente,",","o curso desejado com desconto ficou: R$",valorCurso-desconto)
    elif curso == 5:
        valorCurso = 300
        desconto = valorCurso * idade / 100
        print(greeting,cliente,",","o curso desejado com desconto ficou: R$",valorCurso-desconto)
    else:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True