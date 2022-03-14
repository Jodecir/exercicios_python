import random

numMax = 3
numMin = 1
objetoPLR = 0
partidas = 0
vitorias = 0
derrotas = 0
empates = 0

def pulaLinha():
    print("---------------------")

def opcoesObjeto():
    print(">> [1]: Pedra 🗿")
    print(">> [2]: Papel 📜")
    print(">> [3]: Tesoura ✂️")

def scoreBoard():
    print(f"Quantidade de partidas: {partidas}")
    print(f"Quantidade de vitórias: {vitorias}")
    print(f"Quantidade de derrotas: {derrotas}")
    print(f"Quantidade de empates: {empates}")

fechado = False

while fechado == False:
    try:
        opcoesObjeto()

        objetoPLR = int(input('Escolha o número do objetoPLR: '))
        while objetoPLR > numMax or objetoPLR < numMin:
            opcoesObjeto()
            objetoPLR = int(input('Escolha um número VÁLIDO na LISTA: '))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        objetoCPU = random.randint(numMin, numMax)

        if objetoPLR == objetoCPU:
            print(">> [Você empatou com a CPU]")
            partidas += 1
            empates += 1
        elif objetoPLR == 1 and objetoCPU == 2:
            print(">> [Você]:   Pedra 🗿")
            print(">> [CPU]:    Papel 📜")
            partidas += 1
            derrotas += 1
        elif objetoCPU == 1 and objetoPLR == 2:
            print(">> [Você]:   Papel 📜")
            print(">> [CPU]:    Pedra 🗿")
            partidas += 1
            vitorias += 1
        elif objetoPLR == 2 and objetoCPU == 3:
            print(">> [Você]:   Papel 📜")
            print(">> [CPU]:    Tesoura ✂️")
            partidas += 1
            derrotas += 1
        elif objetoCPU == 2 and objetoPLR == 3:
            print(">> [Você]:   Tesoura ✂️")
            print(">> [CPU]:    Papel 📜")
            partidas += 1
            vitorias += 1
        elif objetoPLR == 3 and objetoCPU == 1:
            print(">> [Você]:   Tesoura ✂️")
            print(">> [CPU]:    Pedra 🗿")
            partidas += 1
            derrotas += 1
        elif objetoCPU == 3 and objetoPLR == 1:
            print(">> [Você]:   Pedra 🗿")
            print(">> [CPU]:    Tesoura ✂️")
            partidas += 1
            vitorias += 1
        else: 
            print("Erro Inesperado")
    finally:
        pulaLinha()
        scoreBoard()
        pulaLinha()

        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True