import random

def pulaLinha():
    print("---------------------")

def saldo(a):
    return a

def depositar(a, b):
    if (b > a):
        return 'Operação negada'
    else:
        return a + b

def sacar(a, b):
    if (b > a):
        return 'Operação negada'
    else:
        return a - b

numMax = 90000
numMin = 1
proprietário_ContaBancaria = "Jodecir"
saldo_ContaBancaria = random.randint(numMin, numMax)
saldo_Carteira = 400
agencia_ContaBancaria = random.randint(1, 9999)
numero_ContaBancaria = random.randint(1000000, 999999999)
tipos_ContaBancaria = ("Poupança", "Universitária")
tipo_ContaBancaria = 1
operador = 0

fechado = False

while fechado == False:
    try:
        pulaLinha()
        print(f"Bem vindo, {proprietário_ContaBancaria}")
        pulaLinha()
        print(">> [1]: Ver Saldo")
        print(">> [2]: Depositar")
        print(">> [3]: Sacar")
        print(">> [4]: Sair")
        pulaLinha()
        print("Tipo de Conta: {}".format(tipos_ContaBancaria[tipo_ContaBancaria]))
        print(f"Agência: {agencia_ContaBancaria}")
        print(f"Número da conta: {numero_ContaBancaria}")
        pulaLinha()

        operador = input('>>> Insira o número da operação: ')
        if operador == "1" or operador == "ver" or operador == "saldo":
            saldo_ContaBancaria = saldo(saldo_ContaBancaria)
            print(f"\nSeu saldo é: R${saldo_ContaBancaria:0,.2f}\n")
        elif operador == "2" or operador == "depositar" or operador == "deposito":
            try:
                valor = abs(int(input('\nInsira o valor: ')))
            except FloatingPointError:
                print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
            except ValueError:
                pulaLinha()
                print("Valor inválido. Deve-se digitar apenas números.")
                pulaLinha()
            else:
                while valor > saldo_Carteira:
                    print(f'\nXXXXX Você não tem esse dinheiro para depositar, você tem apenas R${saldo_Carteira:0,.2f}')
                    
                    try:
                        valor = abs(int(input('\nInsira o valor: ')))
                    except FloatingPointError:
                        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
                    except ValueError:
                        pulaLinha()
                        print("Valor inválido. Deve-se digitar apenas números.")
                        pulaLinha()
            saldo_ContaBancaria = depositar(saldo_ContaBancaria, valor)
            saldo_Carteira = sacar(saldo_Carteira, valor)
            print(f"\n>>> dinheiro depositado com sucesso.\n")
            print(f"Seu saldo atual é: R${saldo_ContaBancaria:0,.2f}\n")
        elif operador == "3" or operador == "sacar" or operador == "saque":
            try:
                valor = abs(int(input('\nInsira o valor: ')))
            except FloatingPointError:
                print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
            except ValueError:
                pulaLinha()
                print("Valor inválido. Deve-se digitar apenas números.")
                pulaLinha()
            else:
                while valor > saldo_ContaBancaria:
                    print(f'\nXXXXX Você não tem esse dinheiro para sacar, você tem apenas R${saldo_ContaBancaria:0,.2f}')
                    
                    try:
                        valor = abs(int(input('\nInsira o valor: ')))
                    except FloatingPointError:
                        print("Valores flutuantes são inválidos. Deve-se digitar apenas números inteiros.")
                    except ValueError:
                        pulaLinha()
                        print("Valor inválido. Deve-se digitar apenas números.")
                        pulaLinha()
            saldo_ContaBancaria = sacar(saldo_ContaBancaria, valor)
            saldo_Carteira = depositar(saldo_Carteira, valor)
            print(f"\n>>> dinheiro retirado com sucesso.\n")
            print(f"\n>>> Seu saldo atual é: R${saldo_ContaBancaria:0,.2f}\n")
        else:
            pulaLinha()
            print("Operador inválido.")
    finally:
        repetir = input("<<< Deseja continuar a operação (s/n): ")
        if repetir == "n":
            fechado = True