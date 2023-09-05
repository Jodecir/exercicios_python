def letters_count(words_list):
  count = []
  for x in words_list:
    quantity = len(x)
    count.append(quantity)
  return count

def remove_repetidos(lista):
  lista_itens_unicos = []

  for item in lista:
    if(item in lista_itens_unicos): #Verifica se o atual elemento existe na lista original
      pass
    else:
      lista_itens_unicos.append(item) #Se não existir, adiciona com o comando append() o numero na lista

  return lista_itens_unicos

def pulaLinha():
  print("---------------------")

fechado = False

while fechado == False:
  if __name__ == '__main__':
    try:
      animais = ['cachorro', 'gato', 'elefante']
      novoAnimal = input('Digite um animal a lista: \n')

      animais.append(novoAnimal)
      animais = sorted(remove_repetidos(animais))
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