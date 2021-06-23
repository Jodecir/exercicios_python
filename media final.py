nome = input('Insira o nome do Aluno: ')
n1 = float(input('Nota do 1º Bimestre: '))
while n1 > 10:
  n1 = float(input('Nota Acima do Permitido, 1º Bimestre: '))
n2 = float(input('Nota do 2º Bimestre: '))
while n2 > 10:
  n2 = float(input('Nota Acima do Permitido, 2º Bimestre: '))
n3 = float(input('Nota do 3º Bimestre: '))
while n3 > 10:
  n3 = float(input('Nota Acima do Permitido, 3º Bimestre: '))
n4 = float(input('Nota do 4º Bimestre: '))
while n4 > 10:
  n4 = float(input('Nota Acima do Permitido, 4º Bimestre: '))

media = (n1 + n2 + n3 + n4) / 4

if __name__ == '__main__':
  if (media >= 6):
    print("---------------------")
    print("# Matricula:","01234",)
    print("Nome do Aluno:",nome,)
    print("---------------------")
    print("Nota 1º B:", n1)
    print("Nota 2º B:", n2)
    print("Nota 3º B:", n3)
    print("Nota 4º B:", n4)
    print("---------------------")
    print('Média Final: {}'.format(media))
    print(nome,"foi aprovado.",)
  else:
    print("---------------------")
    print("# Matricula:","01234",)
    print("Nome do Aluno:",nome,)
    print("---------------------")
    print("Nota 1º B:", n1)
    print("Nota 2º B:", n2)
    print("Nota 3º B:", n3)
    print("Nota 4º B:", n4)
    print("---------------------")
    print('Sua média é: {}'.format(media))
    print(nome,"foi reprovado.",)