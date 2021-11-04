fechado = False

while fechado == False:
  try:
    idade = int(input('Qual sua idade ? '))

    if idade >= 18:
      print("Você é maior de idade")
    elif idade > 0 & idade < 18:
      print("Você é menor de idade")
    else:
      print("Valor inválido")
  except FloatingPointError:
    print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
  except ValueError:
    print("Valor inválido. Deve-se digitar apenas números.")
  finally:
    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True