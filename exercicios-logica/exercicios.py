def operacoes_matematicas():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        print(f"\nSoma: {a + b}")
        print(f"Subtração: {a - b}")
        print(f"Multiplicação: {a * b}")

        if b != 0:
            print(f"Divisão: {a / b}")
        else:
            print("Divisão: não é possível dividir por zero.")
    except ValueError:
        print("Entrada inválida!")


def par_ou_impar():
    try:
        num = int(input("Digite um número: "))
        if num % 2 == 0:
            print("O número é PAR.")
        else:
            print("O número é ÍMPAR.")
    except ValueError:
        print("Entrada inválida!")


def tabuada():
    try:
        num = int(input("Digite um número para ver a tabuada: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Entrada inválida!")


def soma_lista():
    lista = [1,2,3,4,5,6,7,8,9]
    soma = 0
    for n in lista:
        soma += n
    print(f"Lista: {lista}")
    print(f"Soma: {soma}")


def maior_menor():
    lista = [10, 9, 8, 1, 7, 12, 6, 5]
    maior = lista[0]
    menor = lista[0]

    for n in lista:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    print(f"Lista: {lista}")
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")


def fibonacci_iterativo():
    try:
        n = int(input("Quantos números da sequência Fibonacci? "))

        if n <= 0:
            print("Informe um número maior que zero.")
            return

        anterior = 0
        atual = 1

        print("\nSequência:")
        if n >= 1:
            print(anterior)
        if n >= 2:
            print(atual)

        for _ in range(n - 2):
            proximo = anterior + atual
            print(proximo)
            anterior = atual
            atual = proximo

    except ValueError:
        print("Entrada inválida!")


def fibonacci_recursivo():
    def fibonacci(n):
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    try:
        n = int(input("Digite a posição do Fibonacci: "))
        print(f"Resultado: {fibonacci(n)}")
    except ValueError:
        print("Entrada inválida!")


def inverter_lista():
    lista = [4, 2, 3, 5]
    lista_reversa = []

    for n in lista:
        lista_reversa.insert(0, n)

    print(f"Lista original: {lista}")
    print(f"Lista invertida: {lista_reversa}")


def contar_vogais():
    palavra = input("Digite uma palavra: ")
    qtd = 0

    for letra in palavra:
        if letra.lower() in "aeiou":
            qtd += 1

    print(f"Quantidade de vogais: {qtd}")


# ===================== MENU PRINCIPAL =====================

while True:
    print("\n========= MENU =========")
    print("1 - Operações matemáticas   6 - Fibonacci (iterativo)")
    print("2 - Par ou ímpar            7 - Fibonacci (recursivo)")
    print("3 - Tabuada                 8 - Inverter lista")
    print("4 - Soma de lista           9 - Contar vogais")
    print("5 - Maior e menor           0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        operacoes_matematicas()

    elif opcao == "2":
        par_ou_impar()

    elif opcao == "3":
        tabuada()

    elif opcao == "4":
        soma_lista()

    elif opcao == "5":
        maior_menor()

    elif opcao == "6":
        fibonacci_iterativo()

    elif opcao == "7":
        fibonacci_recursivo()

    elif opcao == "8":
        inverter_lista()

    elif opcao == "9":
        contar_vogais()

    elif opcao == "0":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida!")
