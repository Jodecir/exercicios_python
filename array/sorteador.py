import random

fechado = False

while fechado == False:
  if __name__ == '__main__':
    try:
      n1 = input('Insira o primeiro valor: ')
      n2 = input('Insira o segundo valor: ')
      n3 = input('Insira o terceiro valor: ')
      n4 = input('Insira o quarto valor: ')
    except IndexError:
      print('Não foi possível acessar o index pois ele não existe na lista')
    except Exception:
      print('Ocorreu um erro desconhecido')
    else:
      lista = [n1, n2, n3, n4]

      unico = random.choice(lista)
      print(f'O valor único escolhido foi {unico}')
      
      random.shuffle(lista)
      print('O valor ordenado escolhido foi:')
      print(lista)
    finally:
      repetir = input("Deseja continuar (s/n): ")
      if repetir == "n":
        fechado = True