def pulaLinha():
    print("---------------------")

def imc(a, b):
    return a / (b * b)

fechado = False

while fechado == False:
    try:
        print('Calculos:')
        nome = str(input('Insira o nome: ').capitalize())
        altura = float(input('Insira altura: '))
        peso = int(input('Insira o peso: '))
    except FloatingPointError:
        print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        imc = imc(peso, altura)

        if imc <= 16:
            pulaLinha()
            print(f'{nome} está gravemente abaixo do peso.')
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        elif imc >= 16 and imc <= 16.9:
            pulaLinha()
            print(f'{nome} está moderadamente abaixo do peso.')
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        elif imc >= 17 and imc <= 18.4:
            pulaLinha()
            print(f'{nome} está levemente abaixo do peso.')
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        elif imc >= 18.5 and imc <= 24.9:
            pulaLinha()
            print(f'{nome} está em um peso saudável.')
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        elif imc >= 25 and imc <= 29.9:
            pulaLinha()
            print(f'{nome} está em pobrepeso.')
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        elif imc >= 30:
            pulaLinha()
            print(f'{nome} está com obesidade.')
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        elif imc >= 30:
            pulaLinha()
            print(f'{nome} está com obesidade severa.')   
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        elif imc >= 40:
            pulaLinha()
            print(f'{nome} precisa de tratamento, isso é obesidade mórbida!')    
            pulaLinha()
            print('Seu imc é %.1f'% (imc))
            pulaLinha()
        else:
            pulaLinha()
            print(f'{nome} refaça o teste por favor, algo está incorreto.')
            pulaLinha()
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True