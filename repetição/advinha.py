import random

numMax = 100
numMin = 1
numRandom = random.randint(numMin, numMax)  # sorteia número entre 1 e 100
cnt = 0
guess = 0

fechado = False

while fechado == False:
    while guess != numRandom:
        try:
            guess = int(input('Chute um número de 1 a 100: '))
        except FloatingPointError:
            print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
        except ValueError:
            print("Valor inválido. Deve-se digitar apenas números.")
        else:
            while guess > numMax or guess < numMin:
                guess = int(input('Seu número está incorreto, chute um número de 1 a 100: '))
            cnt += 1

            if guess < numRandom:
                print ("Errou, o número sorteado é Maior")
            elif guess > numRandom:
                print ("Errou, o número sorteado é Menor")
            else:
                print("---------------------")
                print(">>> Parabéns, você tem muita sorte e acertou!")
                print("---------------------")
                print("Tentativas necessárias:", cnt)
                print("---------------------")
        
                repetir = input("Deseja continuar (s/n): ")
                if repetir == "n":
                    fechado = True