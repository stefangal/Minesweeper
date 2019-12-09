import pygame
from pygame.locals import *
from backend import Array


pygame.init()
np_board = Array(31,20)
font = pygame.font.SysFont(None, 30)

W = 805
H= 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (120,120,120)

screen = pygame.display.set_mode((W, H))
flag_img = pygame.image.load("flag.png").convert_alpha()
flag_img = pygame.transform.scale(flag_img, (23,23))
bomb_img = pygame.image.load("bomb.png").convert_alpha()

bomb_img = pygame.transform.scale(bomb_img, (23,23))

clock = pygame.time.Clock()
game = True

def events():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == QUIT:
            pygame.quit()

def board(surface):
    for a, x in enumerate(range(15, W-20, 25)):
        for b, y in enumerate(range(90,H-10, 25)):
            if np_board.board[a][b] == 0:
                pygame.draw.rect(surface, WHITE, [x, y, 23,23], 0)
            elif np_board.board[a][b] > 0:
                text = font.render(str(np_board.board[a][b]), True, (0, 128, 0))
                pygame.draw.rect(surface, WHITE, [x, y, 23,23], 0)
                surface.blit(text, (x+5,y+2))
                # pygame.draw.rect(surface, RED, [x, y, 23,23], 0)
            elif np_board.board[a][b] == -1:
                pygame.draw.rect(surface, RED, [x, y, 23,23], 0)
                screen.blit(bomb_img,(x, y))

def fullist():
    lst = []
    for x in range(len(np_board.board)):
        for y in range(len(np_board.board[0])):
            if x == 0:
                startX = 15
                endX = startX + 25
            elif x > 0:
                startX = 15+ x*25
                endX = startX + 25
            if y == 0:
                startY = 90
                endY = startY + 25
            elif y > 0:
                startY = 90 + y*25
                endY = startY + 25
            for a in range(startX, endX):
                for b in range(startY, endY):
                    lst.append([a, b])
    return lst


def safelist():
    lst = []
    for x in range(len(np_board.board)):
        for y in range(len(np_board.board[0])):
            if np_board.board[x][y] == 1:
                if x == 0:
                    startX = 15
                    endX = startX + 25
                elif x > 0:
                    startX = 15+ x*25
                    endX = startX + 25
                if y == 0:
                    startY = 90
                    endY = startY + 25
                elif y > 0:
                    startY = 90 + y*25
                    endY = startY + 25
                for a in range(startX, endX):
                    for b in range(startY, endY):
                        lst.append([a, b])

    return lst

def cover(surface):

    for a, x in enumerate(range(15, W-20, 25)):
        for b, y in enumerate(range(90,H-10, 25)):
            pygame.draw.rect(surface, GREY, [x, y, 23,23], 0)

def bomb(mx, my):
    if [mx, my] in safelist():
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)


while game:
    clock.tick(50)
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    events()
    board(screen)

    #cover(screen)
    screen.blit(flag_img,(90,115))

    bomb(mouse_x, mouse_y)
    pygame.display.update()

pygame.quit()