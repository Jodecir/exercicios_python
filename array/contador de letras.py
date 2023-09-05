def letters_count(words_list):
  count = []
  for x in words_list:
    quantity = len(x)
    count.append(quantity)
  return count

def pulaLinha():
    print("---------------------")

fechado = False

while fechado == False:
  if __name__ == '__main__':
    try:
      animais = ['cachorro', 'gato', 'elefante']
      novoAnimal = input('Digite um animal a lista: \n')

      animais.append(novoAnimal)
      total_letters = letters_count(animais)
      
      pulaLinha()
      print('Animais da lista:')
      for animal in animais:
        print(f'{animal}')
      pulaLinha()
      print('Total de letras por palavra da lista: {}'.format(total_letters))
      pulaLinha()
    except IndexError:
      print('Não foi possível acessar o index pois ele não existe na lista')
    except Exception:
      print('Ocorreu um erro desconhecido')
    finally:
      repetir = input("Deseja continuar (s/n): ")
      if repetir == "n":
        fechado = True