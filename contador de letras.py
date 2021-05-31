def letters_count(lista_palavras):
  count = []
  for x in lista_palavras:
    quantity = len(x)
    count.append(quantity)
  return count

if __name__ == '__main__':
  lista_animais = ['cachorro', 'gato', 'elefante']
  total_letters = letters_count(lista_animais)
  print('total de letras por palavra da lista: {}'.format(total_letters))