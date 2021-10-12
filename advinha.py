import random

numMax = 100
numMin = 1
numRandom = random.randint(numMin, numMax)  # sorteia número entre 1 e 100
cnt = 0
guess = 0

while guess != numRandom:
    try:
        guess = int(input('Chute um número de 1 a 100: '))
        while guess > numMax or guess < numMin:
            guess = int(input('Seu número está incorreto, chute um número de 1 a 100: '))
        cnt += 1

        if guess < numRandom:
            print ("Errou, o número sorteado é Maior")
        elif guess > numRandom:
            print ("Errou, o número sorteado é Menor")
        else:
            print(">>> Acertou! Parabéns, você é um gênio!")
            print(">>> Precisou de", cnt, "tentativas.")
    except ValueError:
        print('Valor inválido, digite apenas números.')