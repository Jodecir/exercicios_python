fechado = False

while fechado == False:
    if __name__ == '__main__':
        try:
            fatorial = int(input("Fatorial de: "))
        except FloatingPointError:
            print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
        except ValueError:
            print("Valor inválido. Deve-se digitar apenas números.")
        else:
            multiplicação = 1
            
            if int(fatorial) >= 1:
                for i in range (1,int(fatorial) + 1):
                    multiplicação *= i

            resultado = multiplicação
            print("{}! = {}".format(fatorial, resultado));
        finally:
            repetir = input("Deseja continuar (s/n): ")
            if repetir == "n":
                fechado = True