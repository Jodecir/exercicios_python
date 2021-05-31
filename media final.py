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
    print('Sua média é: {}'.format(media))
    print("Você foi Aprovado")
  else:
    print('Sua média é: {}'.format(media))
    print("Você foi Reprovado")