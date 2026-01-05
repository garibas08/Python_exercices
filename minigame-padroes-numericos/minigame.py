lista = []
tamanho_lista = int(input("Escolha uma quantidade de números que deseja guardar (2-9):\n\n"))
while tamanho_lista < 2 or tamanho_lista > 9 :
        tamanho_lista = int(input(" insira valores válidos de 2 a 9:\n\n"))
     
print(f"digite {tamanho_lista} numero(s): \n")

for i in range(tamanho_lista):

    item = int(input(f"numero {i+1}: "))
    lista.append(item)

crescente = True
decrescente = True
constante = True

for j in range(tamanho_lista - 1):

    if lista[j] > lista [j+1] or lista[j] == lista [j+1]:
        crescente = False 
    if lista[j] < lista [j+1] or lista[j] == lista [j+1]:
        decrescente = False 
    if lista[j] != lista [j+1]:
        constante = False 

if crescente == True:
    tipo = "crescente"
elif decrescente == True:
    tipo = "decrescente"
elif constante == True:
    tipo = "constante"
else:
    tipo = "sem padrão"

print(f"\n o tipo da lista é: {tipo}\n os números são: ", lista)