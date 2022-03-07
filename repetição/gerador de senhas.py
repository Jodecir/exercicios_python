import random, string

def pulaLinha():
    print("---------------------")

fechado = False

while fechado == False:
    defaultSize = 8
    bigSize = 16

    chars = string.ascii_uppercase + string.ascii_letters + string.digits + string.digits + '!@#$*?'

    rnd = random.SystemRandom()

    pulaLinha()
    print("Senha forte de 8 dígitos:")
    print(''.join(rnd.choice(chars) for i in range(defaultSize)))
    pulaLinha()
    print("Senha extremamente forte de 16 dígitos:")
    print(''.join(rnd.choice(chars) for i in range(bigSize)))
    pulaLinha()

    repetir = input("Deseja gerar outra senha (s/n): ")
    if repetir == "n":
        fechado = True