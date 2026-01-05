
def buscar_saida(labirinto, linha, coluna):#função recursiva para achar a saida

    #verifica o tamanho da matriz para garantir que não fique em um loop
    if linha < 0 or linha >= len(labirinto) or coluna < 0 or coluna >= len(labirinto[0]): 
        return False

    #verifica se pode continuar andando, se for 1 = parede = false/não pode prosseguir ou se já foo visitada "V"
    if labirinto[linha][coluna] == 1 or labirinto[linha][coluna] == 'V':
        return False

    #Se a casa que esta sendo verificada tiver o valor de S quer dizer que saiu do labirinto 
    if labirinto[linha][coluna] == 'S':
        return True

    # marca como visitado
    labirinto[linha][coluna] = 'V'

    if (
        #direções possíveis para andar 
        buscar_saida(labirinto, linha + 1, coluna) or
        buscar_saida(labirinto, linha - 1, coluna) or
        buscar_saida(labirinto, linha, coluna + 1) or
        buscar_saida(labirinto, linha, coluna - 1)
    ):
        # caminho certo
        labirinto[linha][coluna] = '.'
        return True

    return False

def encontrar_entrada(labirinto): #funcao para achar a entrada "E"
    for i in range(len(labirinto)):
        for j in range(len(labirinto[0])):
            if labirinto[i][j] == 'E':
                return i, j
    return None


def imprimir_labirinto(lab): #funcao para imprimir o caminho percorrido
    for linha in lab:
        print(" ".join(str(c) for c in linha))


labirinto = [
    ['E',1,0,0,0,0],
    [0,1,0,1,1,0],
    [0,1,0,1,1,0],
    [0,1,0,'S',1,0],
    [0,1,1,0,1,0],
    [0,0,0,0,0,0]
]

entrada = encontrar_entrada(labirinto)

#verifica se o valor encontrado é entrada e faz a chamada recursiva
if entrada:
    linha, coluna = entrada
    buscar_saida(labirinto, linha, coluna)


#chamadas recursivas
imprimir_labirinto(labirinto)


