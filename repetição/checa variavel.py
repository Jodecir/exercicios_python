fechado = False

while fechado == False:
  variavel = str(input("Digite algo: "))

  print("O tipo primitivo desse valor é {}".format(type(variavel)))
  print("Só tem espaços: {}".format(variavel.isspace()))
  print("---------------------")
  print("É alfabético: {}".format(variavel.isalpha()))
  print("É alfanumérico: {}".format(variavel.isalnum()))
  print("É um título: {}".format(variavel.istitle()))
  print("É um número: {}".format(variavel.isnumeric()))
  print("---------------------")
  print("É maiúscula: {}".format(variavel.isupper()))
  print("É minúsculo: {}".format(variavel.islower()))
  print("---------------------")
  print("Tem: {} caracteres (contando espaços)".format(len(variavel)))
  print("Tem: {} caracteres (sem espaços)".format(len(variavel) - variavel.count(' ')))
  print("---------------------")

  repetir = input("Deseja continuar (s/n): ")
  if repetir == "n":
      fechado = True