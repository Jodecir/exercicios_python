fechado = False

while fechado == False:
  try:
    print('Calculos:')
    nome = input('Qual o seu nome: ')
    altura = float(input('Qual sua altura ? '))
    peso = int(input('Qual seu peso ? '))
    imc = peso / (altura * altura)

    if imc <= 18.5:
      print("---------------------")
      print(nome + ' está abaixo do peso.')
      print("---------------------")
      print('Seu imc é', imc) 
      print("---------------------")
    elif imc >= 18.5 and imc <= 24.9:
      print("---------------------")
      print(nome + ' está no peso normal.')
      print("---------------------")
      print('Seu imc é', imc) 
      print("---------------------")
    elif imc >= 25 and imc <= 29.9:
      print("---------------------")
      print(nome + ' está em pobrepeso.')
      print("---------------------")
      print('Seu imc é', imc) 
      print("---------------------")
    elif imc >= 30:
      print("---------------------")
      print(nome + ' precisa de tratamento, isso é obesidade!')      
      print("---------------------")
      print('Seu imc é', imc) 
      print("---------------------")
    else:
      print("---------------------")
      print(nome + ' refaça o teste por favor, algo está incorreto.')
      print("---------------------")
  except FloatingPointError:
    print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
  except ValueError:
    print("Valor inválido. Deve-se digitar apenas números.")
  finally:
    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True