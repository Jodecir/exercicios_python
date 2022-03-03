fechado = False

while fechado == False:
  try:
    idade = int(input('Insira sua idade: '))
  except FloatingPointError:
    print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
  except ValueError:
    print("Valor inválido. Deve-se digitar apenas números.")
  else:
    maiorIdade = 18

    if idade >= maiorIdade:
      print("\n Você é maior de idade.\n")
    elif idade > 0 & idade < maiorIdade:
      print("\n Você é menor de idade.\n")
    else:
      print("\n Valor inválido \n")
  finally:
    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True