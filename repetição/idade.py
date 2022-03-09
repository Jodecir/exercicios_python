fechado = False

while fechado == False:
    try:
        idade = int(input('Insira sua idade: '))
    except FloatingPointError:
        print("Valores flutuantes são inválido. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        maiorIdade = 18
        idadeVoto = 16

        if idade >= maiorIdade:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade")
        if idade >= idadeVoto:
            print("Já pode votar.")
        else:
            print("Não pode votar")
        if idade > 0 and idade < maiorIdade:
            print("Ainda vai se alistar")
        elif idade > maiorIdade:
            print("Passou do tempo de se alistar")
        else:
            print("Tá na hora de se alistar")
    finally:
        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True