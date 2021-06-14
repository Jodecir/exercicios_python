print('Calculos:')
a = int(input('Insira o Primeiro Valor: '))
b = int(input('Insira o Segundo Valor: '))
soma              = a + b
subtracao         = a - b
multiplicacao     = a * b
divisao           = a / b
media             = int((a + b) / 2)
resultado = ('Soma: {soma} \nSubtração: {subtracao} '
      '\nMultiplicação: {multiplicacao}'
      '\nDivisão: {divisao}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao))

print(resultado)
print('Média: ' + str(media))