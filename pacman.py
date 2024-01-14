from random import randint
from getch import getch
from os import system


def spawn_pos():
    return randint(0, 9)


def pcm_get_pos(pcm_init_pos):
    pcm_init_pos[0] = spawn_pos()
    pcm_init_pos[1] = spawn_pos()


def gxt_get_pos(gxt_init_pos):
    gxt_init_pos[0] = spawn_pos()
    gxt_init_pos[1] = spawn_pos()


def gxt_move(gxt_init_pos):
    choice = randint(0, 3)
    if choice == 0 and gxt_init_pos[0] > 0:
        gxt_init_pos[0] -= 1
    if choice == 1 and gxt_init_pos[0] < 9:
        gxt_init_pos[0] += 1
    if choice == 2 and gxt_init_pos[1] > 0:
        gxt_init_pos[1] -= 1
    if choice == 3 and gxt_init_pos[1] < 9:
        gxt_init_pos[1] += 1
    else:
        gxt_init_pos = gxt_init_pos


pcm_init_pos = [None]*2
gxt_init_pos = [spawn_pos(), spawn_pos()]

pcm_get_pos(pcm_init_pos)
while gxt_init_pos[0] == pcm_init_pos[0] and gxt_init_pos[1] == pcm_init_pos[1]:
    gxt_get_pos(gxt_init_pos)

game_status = True

while game_status:
    gxt_move(gxt_init_pos)
    system('clear')
    for i in range(10):
        for j in range(10):
            if pcm_init_pos[0] == i and pcm_init_pos[1] == j:
                print('x ', end="")
            elif gxt_init_pos[0] == i and gxt_init_pos[1] == j:
                print('0 ', end="")
            else:
                print('. ', end="")
        print()
    move = getch()
    if move.upper() == 'W' and pcm_init_pos[0] != 0:
        pcm_init_pos[0] -= 1
    if move.upper() == 'S' and pcm_init_pos[0] != 9:
        pcm_init_pos[0] += 1
    if move.upper() == 'A' and pcm_init_pos[1] != 0:
        pcm_init_pos[1] -= 1
    if move.upper() == 'D' and pcm_init_pos[1] != 9:
        pcm_init_pos[1] += 1

    if pcm_init_pos[0] == gxt_init_pos[0] and pcm_init_pos[1] == gxt_init_pos[1]:
        game_status = False

print("GAME OVER")
