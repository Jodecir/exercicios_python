n1 = int(input("Digite um número: "))
count = 1

if __name__ == '__main__':
  while count <= n1:
    if n1 % 2 == 1 and n1 >= 2:
        count = count + 1
        print("Número primo")
        break
    else:
        print("Número não primo")
        break