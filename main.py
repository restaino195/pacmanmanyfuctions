from utils import floor
from turtle import *
import numpy as np
import random

def ler_matriz():
    return [[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],\
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]]

def criar_labirinto(p1=420, p2=420, p3=370, p4=0):
    tracer(False)
    hideturtle()
    bgcolor('black')
    setup(p1, p2, p3, p4)
    for lin in range(dim):
        for col in range(dim):
            if (matriz[lin][col] == 1):
                x, y = em_coord_turtle(lin, col)
                desenhar_celula(x, y, 'blue')
                desenhar_pastilha(x, y, 'white')
    update()

def desenhar_celula(x, y, cor):
    color(cor)
    up()
    goto(x,y)
    down()
    begin_fill()
    for _ in range(4):
        forward(tam_celula)
        left(90)
    end_fill()
    up()

def teste1_transf_coord_funcionou():
    for lin in range(dim):
        for col in range(dim):
            x, y = em_coord_turtle(lin, col)
            if ( not (lin, col) == em_coord_matriz(x, y) ):
                return False
    return True

def teste2_transf_coord_funcionou():
    meio = dim // 2
    tam_celula = 20
    n = meio * tam_celula * 10
    for k1 in range(-n, n,5):
        for k2 in range(n, -n, -5):
            x = k1 / 10
            y = k2 / 10
            lin, col = em_coord_matriz(x, y)
            if (not chao_da_celula(x, y) == em_coord_turtle(lin, col) ):
                return False
    return True

def testar_transf_de_coord():
    if (teste1_transf_coord_funcionou() and \
        teste2_transf_coord_funcionou()):
        return "Todas as transformações de coordenadas funcionaram"
    else:
        return "As transformações de coordenadas não funcionaram"


def uso_do_floor():
    for i in range(-200,200):
        print("{}\t{}".format(i, int(floor(i, 20)) ))

def chao_da_celula(x, y):
      chao_x = int(floor(x, tam_celula))
      chao_y = int(floor(y, tam_celula))
      return chao_x, chao_y

def em_coord_turtle(lin, col):
    meio = dim // 2
    x = (col - meio) * tam_celula
    y = (meio - lin) * tam_celula
    return x, y

def adicionar_agente():
    dim = len(matriz)
    lin, col = cel_aleatoria()
    x, y = em_coord_turtle(lin, col)
    desenhar_agente(x, y, 'yellow')

def em_coord_matriz(x, y):
    chao_x= x + i * tam_celula
    chao_y= y + j * tam_celula
    turtle.goto(chao_x, chao_y)
    pass

def ler_matriz_aleatoria(dim):
    matriz = []
    for i in range(dim):
        linha = []
        for j in range(dim):
            valor = random.randrange (2)
            linha.append(valor)
        matriz.append(linha)
    pass

def cel_aleatoria():
    matriz = []
    for i in range(dim):
        linha = []
        for j in range(dim):
            valor = int(str(i)) is not int(str(j))
            linha.append(valor)
        matriz.append(linha)
    return matriz
    pass

def eh_caminho(lin, col):
    """ Dada uma matriz quadrada, retorna True quando (lin, col) == 1 e
        False caso contrário.
        Por exemplo, na matriz a seguir:
        [[ 1  0  0 ]
         [ 0  1  0 ]
         [ 0  0  1 ]]
        a chamada de função 'eh_caminho(0,0,matriz)' retorna True e
        a chamada de função 'eh_caminho(0,1,matriz)' retorna False
    """
    # IMPLEMENTE ESSA FUNÇÃO
    pass

def desenhar_agente(x, y, cor):
    """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
        para representar o agente (i.e., pacman, fantasmas)
    """
    # IMPLEMENTE ESSA FUNÇÃO
    pass

def desenhar_pastilha(x, y, cor):
    """ Leva a tartaruga até a posição (x,y) e desenha por exemplo um círculo
        para representar a pastilha
    """
    # IMPLEMENTE ESSA FUNÇÃO
    pass

#matriz = ler_matriz_fixa()
matriz = ler_matriz_aleatoria(20)
dim = len(matriz)
tam_celula = dim
tam_agente = dim

def main():

    criar_labirinto()
    adicionar_agente()
    done()

    # Utilize esse comando para testar se as trasnformações das coordenadas
    # estão funcionando. Ao final da execução, o resultado deve ser que
    # todas as transformações funcionaram
    print(testar_transf_de_coord())

main()
