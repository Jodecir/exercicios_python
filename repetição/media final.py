def pulaLinha():
    print("---------------------")

def media(a, b, c, d):
    return (a + b + c + d) / 4

fechado = False

while fechado == False:
    nome = str(input('Insira o nome do Aluno: ')).capitalize()
    try:
        min = 0
        max = 10
        n1 = float(input('Nota do 1º Bimestre: '))
        while n1 > max or n1 < min:
            n1 = float(input('Nota não permitida, 1º Bimestre: '))
        n2 = float(input('Nota do 2º Bimestre: '))
        while n2 > max or n1 < min:
            n2 = float(input('Nota não permitida, 2º Bimestre: '))
        n3 = float(input('Nota do 3º Bimestre: '))
        while n3 > max or n1 < min:
            n3 = float(input('Nota não permitida, 3º Bimestre: '))
        n4 = float(input('Nota do 4º Bimestre: '))
        while n4 > max or n1 < min:
            n4 = float(input('Nota não permitida, 4º Bimestre: '))
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        media = int(media(n1, n2, n3, n4))

        if __name__ == '__main__':
            pulaLinha()
            print("# Matricula:","01234",)
            print("Nome do Aluno:", nome,)
            pulaLinha()
            print("Nota 1º B:", n1)
            print("Nota 2º B:", n2)
            print("Nota 3º B:", n3)
            print("Nota 4º B:", n4)
            pulaLinha()
            print('Sua média é: {}'.format(media))

            if (media >= 6):
                pulaLinha()
                print(">>>", nome, "foi aprovado.",)
                pulaLinha()
            else:
                pulaLinha()
                print(">>>", nome, "foi reprovado.",)
                pulaLinha()
    finally:
        repetir = input("Deseja continuar (s/n): ")
        pulaLinha()
        if repetir == "n":
            fechado = True