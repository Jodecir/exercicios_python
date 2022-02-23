def aoQuadrado (a):
    return a ** 2

def raiz (a):
    return a ** (1/2)

fechado = False

while fechado == False:
    if __name__ == '__main__':
        try:
            catOp = float(input("Insira o comprimento do cateto oposto: "))
            catAd = float(input("Insira o comprimento do cateto adjacente: "))
        except ValueError:
            print("Valor inválido. Deve-se digitar apenas números.")
        else:
            hipo = raiz((aoQuadrado(catOp)) + (aoQuadrado(catAd)))
            
            print("---------------------")
            resultado = print(f"O comprimento da hipotenusa é {hipo}")
            print("---------------------")
        finally:
            repetir = input("Deseja continuar (s/n): ")
            if repetir == "n":
                fechado = True