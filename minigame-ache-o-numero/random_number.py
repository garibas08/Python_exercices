import random

tentativas = 0
numero_secreto = random.randint(1, 100)

print("Olá, seja bem vindo ao Ache o Número!")

while True:
    palpite = int(input("Escolha um número de 0 a 100: \n\n\n"))

    tentativas += 1

    if palpite > numero_secreto:
        print("Muito alto")

    elif palpite < numero_secreto:
        print("Muito baixo")

    else:
        print("Parabéns você acertou!")
        print(f"Quantidade de tentativas:{tentativas}!")
        break

