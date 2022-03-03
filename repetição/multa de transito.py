fechado = False

while fechado == False:
    try:
        min = 1
        kmCorrido = float(input('Quantos Km/h o carro está: '))
        while kmCorrido < min:
            kmCorrido = float(input('Kilometragem abaixo do permitido, Km/h: '))
        kmMaxPermitido = float(input('Qual a kilometragem máxima permitida: '))
        while kmMaxPermitido < min:
            kmMaxPermitido = float(input('Kilometragem abaixo do permitido, Insira novamente: '))
        valor = float(input('Qual o valor da multa em R$ para cada km excedido: '))
        while valor < min:
            valor = float(input('Valor abaixo do permitido, insira o valor em R$ para cada km excedido: '))
    except ValueError:
        print("Valor inválido. Deve-se digitar apenas números.")
    else:  
        multa = (kmCorrido - kmMaxPermitido) * valor

        if kmCorrido > kmMaxPermitido:
            print("---------------------")
            print(f'Você excedeu o limite permitido de velocidade e terá que pagar uma multa de R${multa:.2f}')
            print("---------------------")
        else:
            print("---------------------")
            print('Você está na velocidade permitida')
            print("---------------------")