import random
from celda import Celda
HEIGH = 3
WIDHT = 3  
MINES = 3


def mines_position():
    mines_place = []
    for i in range(MINES):
        while True:
            x = random.randint(0,(WIDHT-1))
            y =random.randint(0,(HEIGH-1))
            mines_place.append([x,y])
            if i == mines_place.index([x,y]):
                break
            else:
                mines_place.pop(i)
    return mines_place


def game_matriz():
    mines_place = mines_position()
    matriz = []
    for i in range(WIDHT):
        matriz.append([0]*HEIGH)
    for val in mines_place:
        x = val[0]
        y = val[1]
        matriz[x][y] = 9 
    return matriz

def around(x,y):
    around = []
    to_remove = []
    around.append([(x-1),(y-1)])
    around.append([(x-1),(y)])
    around.append([(x-1),(y+1)])
    around.append([(x),(y-1)])
    around.append([(x),(y+1)])
    around.append([(x+1),(y-1)])
    around.append([(x+1),(y)])
    around.append([(x+1),(y+1)])
    for val in around:
        if val[0]==-1 or val[1]==-1 or (val[0]>=HEIGH) or (val[1]>=WIDHT) or (val[0]>=WIDHT) or (val[1]>=HEIGH) :
            to_remove.append(val)
    for rem in to_remove:
        around.remove(rem)
    return  around

def bombs_around(matriz,x,y):
    bombs = 0
    if matriz[x][y] == 9:
        return matriz
    else:
        around_val =around(x,y)
        for val in around_val:
            if matriz[val[0]][val[1]]==9:
                bombs = bombs + 1
        matriz[x][y] = bombs
        return matriz
    
def check_matriz(matriz):
    for x in range(WIDHT):
        for y in range(HEIGH):
            matriz = bombs_around(matriz,x,y) 
    return matriz


        
matriz = game_matriz()

matriz_game = check_matriz(matriz)
for i in range(HEIGH):
    print(matriz_game[i])

print(matriz_game[2][0])

