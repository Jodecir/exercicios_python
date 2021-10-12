try:
  n1 = int(input("Digite um número: "))
except FloatingPointError:
  print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
except ValueError:
  print("Valor inválido. Deve-se digitar apenas números.")
else:
  if __name__ == '__main__':
    if n1 % 2 == 0:
      print("Número Par")
    elif n1 % 2 == 1:
      print("Número Ímpar")
    else:
      print("Valor Inválido")