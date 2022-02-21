import random, string

defaultSize = 8
bigSize = 16

chars = string.ascii_uppercase + string.ascii_letters + string.digits + string.digits + '!@#$*?'

rnd = random.SystemRandom()

print("Senha forte de 8 dígitos:")
print(''.join(rnd.choice(chars) for i in range(defaultSize)))
print("Senha extremamente forte de 16 dígitos:")
print(''.join(rnd.choice(chars) for i in range(bigSize)))