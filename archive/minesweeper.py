import pygame
from pygame.locals import *
from source import Array


pygame.init()
np_board = Array(31,20,2)
print(np_board.board)

font_board = pygame.font.SysFont(None, 30)
font_moves = pygame.font.SysFont(None, 60)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (200,200,200)

W = 805
H= 600

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("M   I   N   E   S   W   E   E   P   E   R")

flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (23,23))
bomb_img = pygame.image.load("bomb.png").convert_alpha()
bomb_img = pygame.transform.scale(bomb_img, (21,21))

# F U N C T I O N S ***********************************************************************

def events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == QUIT:
            pygame.quit()

def board(surface):
    empty_list, touching_list, bomb_list, board_list = [],[],[],[]
    for a, x in enumerate(range(15, W-20, 25)):
        for b, y in enumerate(range(90,H-10, 25)):
            if np_board.board[a][b] == 0:
                pygame.draw.rect(surface, WHITE, [x, y, 23,23], 0)
                empty_list.append([x, y])
            elif np_board.board[a][b] > 0:
                text = font_board.render(str(np_board.board[a][b]), True, (0, 128, 0))
                pygame.draw.rect(surface, WHITE, [x, y, 23,23], 0)
                surface.blit(text, (x+5,y+2))
                touching_list.append([x, y])
            elif np_board.board[a][b] == -1:
                pygame.draw.rect(surface, RED, [x, y, 23,23], 0)
                screen.blit(bomb_img,(x+1, y+1))
                bomb_list.append([x, y])
            elif np_board.board[a][b] == -2:
                surface.blit(flag_img, [x, y])
            board_list.append([x,y])
    return board_list

def cover(surface, lst):
    for a in lst:
        pygame.draw.rect(surface, GREY, [a[0], a[1], 23,23], 0)
    if pygame.mouse.get_pressed()[2]:
        pygame.event.wait()
        x = min(a[0] for a in lst if abs(a[0]-pygame.mouse.get_pos()[0])<24)
        y = min(a[1] for a in lst if abs(a[1]-pygame.mouse.get_pos()[1])<24)
        if [x,y] in lst:
            lst.pop(lst.index([x,y]))

        for a, xx in enumerate(range(15, W-20, 25)):
            for b, yy in enumerate(range(90,H-10, 25)):
                if xx == x and yy == y:
                    np_board.board[a][b] = -2


def clicked(surf, lst, mx, my):
    if pygame.mouse.get_pressed()[0]:
        x = min(a[0] for a in lst if abs(a[0]-mx)<24)
        y = min(a[1] for a in lst if abs(a[1]-my)<24)
        if [x,y] in lst:
            lst.pop(lst.index([x,y]))
            pygame.event.wait()
    return lst

# G A M E *****************************************************************************

start_list = board(screen)
clock = pygame.time.Clock()
game = True
clicked(screen, start_list, *pygame.mouse.get_pos())
top_screen = screen.subsurface(pygame.Rect(W-135, 20, 100, 100 ))

while game:
    clock.tick(20)
    events()
    top_screen.fill((0,0,0))
    board(screen)

    clicked(screen, start_list, *pygame.mouse.get_pos())
    #cover(screen, clicked(screen, start_list, *pygame.mouse.get_pos()))

    move_counter = 620 % len(start_list)
    moves_text = font_moves.render(str(move_counter), True, (255, 0, 0))

    top_screen.blit(moves_text, (10, 10))

    pygame.display.update()

pygame.quit()