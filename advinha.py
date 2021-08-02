import random

num = random.randint(1, 100)  # sorteia número entre 1 e 100
cnt = 0
chute = -1

while chute != num:
    chute = int(input('Chute um número de 1 a 100: '))
    cnt += 1

    if chute < num:
        print ("Errou, o número sorteado é Maior")
    elif chute > num:
        print ("Errou, o número sorteado é Menor")
    else:
        print(">>> Acertou! Parabéns, você é um gênio!")
        print(">>> Precisou de", cnt, "tentativas.")