import re

fechado = False

while fechado == False:
    senha = input("Digite uma Senha: ")
    forca = 0

    if len(senha) >= 4 and len(senha) <= 7:
        forca += 10
    elif len(senha) > 7:
        forca += 15

    if len(senha) > 7 and re.search(r'[a-z]', senha):
        forca += 10

    if len(senha) > 7 and re.search(r'[A-Z]', senha):
        forca += 10

    if len(senha) > 7 and re.search(r'[0-9]', senha):
        forca += 15

    if len(senha) > 7 and re.search(r'[!-+]', senha):
        forca += 20

    if len(senha) > 7 and re.search(r'[a-z]', senha) and re.search(r'[A-Z]', senha) and re.search(r'[0-9]', senha) and re.search(r'[!-+]', senha):
        forca += 20

    if __name__ == '__main__':
        if forca < 30:
            print("Senha Fraca")
        elif forca >= 30 and forca < 50:
            print("Senha Média")
        elif forca >= 50 and forca < 70:
            print("Senha Forte")
        elif forca >= 70 and forca < 100:
            print("Senha Excelente")

        repetir = input("Deseja continuar (s/n): ")
        if repetir == "n":
            fechado = True