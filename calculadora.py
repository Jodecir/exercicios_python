print('Calculos:')
a = int(input('Insira o primeiro valor: '))
b = int(input('Insira o segundo valor: '))
operador = input('Insira o operador entre (+-/*) qualquer outro valor resultará em média: ')
media = int((a + b) / 2)

if operador == "+":
    operacao = a + b
elif operador == "-":
    operacao = a - b
elif operador == "*":
    operacao = a * b
elif operador == "/":
    operacao = a / b
else:
    operacao = "Média igual a " + str(media)

print("Resultado:")
print(operacao)