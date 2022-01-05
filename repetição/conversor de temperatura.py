fechado = False

while fechado == False:
    try:
        n1 = int(input('Insira o valor: '))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        escala = input('Insira a escala que ele está entre (F/C/K): ')
        ctof = (n1 * 1.8) + 32
        ctok = n1 + 273.15
        ftoc = (n1 - 32) / 1.8
        ftok = ((n1 - 32) / 1.8) + 273.15
        ktoc = n1 - 273.15
        ktof = ((n1 - 273.15) * 1.8) + 32
            
        if __name__ == '__main__':
            if escala == "C" or escala == "c":
                print("---------------------")
                print(f">>> A temperatura em F é {ctof}°")
                print("---------------------")
                print(f">>> A temperatura em K é {ctok}°")
                print("---------------------")
            elif escala == "F" or escala == "f":
                print("---------------------")
                print(f">>> A temperatura em C é {ftoc}°")
                print("---------------------")
                print(f">>> A temperatura em K é {ftok}°")
                print("---------------------")
            elif escala == "K" or escala == "k":
                print("---------------------")
                print(f">>> A temperatura em C é {ktoc}°")
                print("---------------------")
                print(f">>> A temperatura em F é {ktof}°")
                print("---------------------")
            else:
                print(">>> Repita o processo por favor, a escala está incorreta.")      
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True