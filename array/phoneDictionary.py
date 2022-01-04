fechado = False

while fechado == False:
    if __name__ == '__main__':
        try:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite seu idade: "))
            telefone = int(input("Digite seu telefone: "))
        except FloatingPointError:
            print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
        except ValueError:
            print("Valor inválido. Deve-se digitar apenas números.")
        else:
            dados = {"nome": nome, "idade": idade, "telefone": telefone,}
            print(dados)

            repetir = input("Deseja continuar (s/n): ")
            if repetir == "n":
                fechado = True