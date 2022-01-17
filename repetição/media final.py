def media(a, b, c, d):
    return (a + b + c + d) / 4

fechado = False

while fechado == False:
    nome = str(input('Insira o nome do Aluno: ')).capitalize()
    try:
        max = 10
        n1 = float(input('Nota do 1º Bimestre: '))
        while n1 > max:
            n1 = float(input('Nota acima do permitido, 1º Bimestre: '))
        n2 = float(input('Nota do 2º Bimestre: '))
        while n2 > max:
            n2 = float(input('Nota acima do permitido, 2º Bimestre: '))
        n3 = float(input('Nota do 3º Bimestre: '))
        while n3 > max:
            n3 = float(input('Nota acima do permitido, 3º Bimestre: '))
        n4 = float(input('Nota do 4º Bimestre: '))
        while n4 > max:
            n4 = float(input('Nota acima do permitido, 4º Bimestre: '))
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        media = int(media(n1, n2, n3, n4))

        if __name__ == '__main__':
            print("---------------------")
            print("# Matricula:","01234",)
            print("Nome do Aluno:", nome,)
            print("---------------------")
            print("Nota 1º B:", n1)
            print("Nota 2º B:", n2)
            print("Nota 3º B:", n3)
            print("Nota 4º B:", n4)
            print("---------------------")
            print('Sua média é: {}'.format(media))

            if (media >= 6):
                print("---------------------")
                print(">>>", nome, "foi aprovado.",)
                print("---------------------")
            else:
                print("---------------------")
                print(">>>", nome, "foi reprovado.",)
                print("---------------------")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        print("...")
        if repetir == "n":
            fechado = True