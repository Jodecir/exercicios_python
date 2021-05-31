n1 = int(input("Digite um número: "))

if __name__ == '__main__':
  if n1 % 2 == 0:
    print("Número Par")
  elif n1 % 2 == 1:
    print("Número Ímpar")
  else:
    print("Valor Inválido")