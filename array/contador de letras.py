def letters_count(words_list):
  count = []
  for x in words_list:
    quantity = len(x)
    count.append(quantity)
  return count

fechado = False

while fechado == False:
  if __name__ == '__main__':
    try:
      animal_list = ['cachorro', 'gato', 'elefante']
      animal = input('Digite um animal a lista: \n')

      animal_list.append(animal)
      total_letters = letters_count(animal_list)

      print('Animais da lista:', animal_list)
      print('Total de letras por palavra da lista: {}'.format(total_letters))
    except IndexError:
      print('Não foi possível acessar o index pois ele não existe na lista')
    except Exception:
      print('Ocorreu um erro desconhecido')
    finally:
      repetir = input("Deseja continuar (s/n): ")
      if repetir == "n":
        fechado = True