print('Calculos:')
nome = input('Qual o seu nome: ')
altura = float(input('Qual sua altura ? '))
peso = int(input('Qual seu peso ? '))
imc = peso / (altura * altura)

if __name__ == '__main__':
  if imc <= 18.5:
    print(nome + ' está abaixo do peso:')
    print(imc)
  elif imc >= 18.5 and imc <= 24.9:
    print(nome + ' está no peso normal:')
    print(imc)
  elif imc >= 25 and imc <= 29.9: 
    print(nome + ' está em pobrepeso:')
    print(imc)
  elif imc >= 30:
    print(nome + ' precisa de tratamento , isso é obesidade!')
    print(imc)
  else:
    print(nome + ' refaça o teste por favor , algo está errado.')