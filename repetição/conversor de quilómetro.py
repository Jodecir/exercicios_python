fechado = False

while fechado == False:
    try:
        n1 = int(input('Insira o valor: '))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        kmToM = n1 * 1000
        kmToCm = n1 * 10000
        kmToMm = n1 * 100000
        kmToMiles = n1 / 1.609
            
        if __name__ == '__main__':
            if n1 >= 0 or n1 <= 0:
                print("---------------------")
                print(f">>> {n1} Km é {kmToM:.0f} metros")
                print(f">>> {n1} Km é {kmToCm:.0f} centimetros")
                print(f">>> {n1} Km é {kmToMm:.0f} milimetros")
                print(f">>> {n1} Km é {kmToMiles:.3f} milhas")
                print("---------------------")
            else:
                print(">>> Repita o processo por favor, o valor está incorreto.")      
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True