import random
import time

numMax = 2
numMin = 0
objetos = ('Pedra', 'Papel', 'Tesoura')
objetoPLR = 0
objetoCPU = 0
partidas = 0
vitorias = 0
derrotas = 0
empates = 0

def pulaLinha():
    print("---------------------")

def objectOptions():
    print(">> [0]: Pedra 🗿")
    print(">> [1]: Papel 📜")
    print(">> [2]: Tesoura ✂️")

def scoreBoard():
    print(f"Partidas: {partidas}")
    print(f"Pontos do Jogador: {vitorias}")
    print(f"Pontos da CPU: {derrotas}")
    print(f"Empates: {empates}")

def playersHands():
    print(">> [Você]:   {}".format(objetos[objetoPLR]))
    print(">> [CPU]:    {}".format(objetos[objetoCPU]))

def handShake():
    print("JO")
    time.sleep(1)
    print("KEN")
    time.sleep(1)
    print("PO")

fechado = False

while fechado == False:
    try:
        objectOptions()

        objetoPLR = int(input('Escolha o número do objetoPLR: '))
        while objetoPLR > numMax or objetoPLR < numMin:
            objectOptions()
            objetoPLR = int(input('Escolha um número VÁLIDO na LISTA: '))
    except FloatingPointError:
        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:
        objetoCPU = random.randint(numMin, numMax)

        if objetoPLR == objetoCPU:
            handShake()
            playersHands()
            partidas += 1
            empates += 1
        elif objetoPLR == 0 and objetoCPU == 1:
            handShake()
            playersHands()
            partidas += 1
            derrotas += 1
        elif objetoCPU == 0 and objetoPLR == 1:
            handShake()
            playersHands()
            partidas += 1
            vitorias += 1
        elif objetoPLR == 1 and objetoCPU == 2:
            handShake()
            playersHands()
            partidas += 1
            derrotas += 1
        elif objetoCPU == 1 and objetoPLR == 2:
            handShake()
            playersHands()
            partidas += 1
            vitorias += 1
        elif objetoPLR == 2 and objetoCPU == 0:
            handShake()
            playersHands()
            partidas += 1
            derrotas += 1
        elif objetoCPU == 2 and objetoPLR == 0:
            handShake()
            playersHands()
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