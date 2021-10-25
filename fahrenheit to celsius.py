fechado = False

while fechado == False:
    try:
        n1 = int(input('Insira o valor: '))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        escala = input('Insira a escala que ele está entre (F/C): ')
        c = (n1 - 32) / 1.8
        f = n1 * 1.8 + 32
            
        if __name__ == '__main__':
            if escala == "C" or escala == "c":
                print("---------------------")
                print(">>> A temperatura em F é", f,"°")
                print("---------------------")
            elif escala == "F" or escala == "f":
                print("---------------------")
                print(">>> A temperatura em C é", c,"°")
                print("---------------------")
            else:
                print(">>> Repita o processo por favor, a escala está incorreta.")      
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True