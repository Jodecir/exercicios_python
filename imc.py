fechado = False

while fechado == False:
  try:
    print('Calculos:')
    nome = input('Qual o seu nome: ')
    altura = float(input('Qual sua altura ? '))
    peso = int(input('Qual seu peso ? '))
    imc = peso / (altura * altura)

    if imc <= 18.5:
      print(nome + ' está abaixo do peso.')
      print('Seu imc é', imc)
    elif imc >= 18.5 and imc <= 24.9:
      print(nome + ' está no peso normal.')
      print('Seu imc é', imc)
    elif imc >= 25 and imc <= 29.9: 
      print(nome + ' está em pobrepeso.')
      print('Seu imc é', imc)
    elif imc >= 30:
      print(nome + ' precisa de tratamento, isso é obesidade!')
      print('Seu imc é', imc)
  except FloatingPointError:
    print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
  except ValueError:
    print("Valor inválido. Deve-se digitar apenas números.")
  else:
    print(nome + ' refaça o teste por favor , algo está errado.')
  finally:
    repetir = input("Deseja continuar (s/n): ")
    if repetir == "n":
        fechado = True