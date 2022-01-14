fechado = False

while fechado == False:
  try:
    print('Calculos:')
    nome = str(input('Insira o nome: ').capitalize())
    altura = float(input('Insira altura: '))
    peso = int(input('Insira o peso: '))
    imc = peso / (altura * altura)

    if imc <= 16:
      print("---------------------")
      print(f'{nome} está gravemente abaixo do peso.')
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    elif imc >= 16 and imc <= 16.9:
      print("---------------------")
      print(f'{nome} está moderadamente abaixo do peso.')
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    elif imc >= 17 and imc <= 18.4:
      print("---------------------")
      print(f'{nome} está levemente abaixo do peso.')
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    elif imc >= 18.5 and imc <= 24.9:
      print("---------------------")
      print(f'{nome} está em um peso saudável.')
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    elif imc >= 25 and imc <= 29.9:
      print("---------------------")
      print(f'{nome} está em pobrepeso.')
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    elif imc >= 30:
      print("---------------------")
      print(f'{nome} está com obesidade.')
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    elif imc >= 30:
      print("---------------------")
      print(f'{nome} está com obesidade severa.')   
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    elif imc >= 40:
      print("---------------------")
      print(f'{nome} precisa de tratamento, isso é obesidade mórbida!')    
      print("---------------------")
      print('Seu imc é %.4f'% (imc))
      print("---------------------")
    else:
      print("---------------------")
      print(f'{nome} refaça o teste por favor, algo está incorreto.')
      print("---------------------")
  except FloatingPointError:
    print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
  except ValueError:
    print("Valor inválido. Deve-se digitar apenas números.")
  finally:
    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True