import pygame
from pygame.locals import *
from backend import Array

class MS:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (200,200,200)
    W = 805
    H = 600
    pygame.display.set_caption("M   I   N   E   S   W   E   E   P   E   R")

    def __init__(self):
        pygame.init()
        self.np_board = Array(31, 20)
        self.bomb_qty = self.np_board.bombs
        self.screen = pygame.display.set_mode((805, 600))

        self.font_board = pygame.font.SysFont(None, 30)
        self.font_header_text = pygame.font.SysFont("Comic Sans MS", 20)
        self.font_header_value = pygame.font.SysFont("Comic Sans MS", 36)

        self.flag_img = pygame.image.load("flag.png").convert_alpha()
        self.flag_img = pygame.transform.scale(self.flag_img, (23,23))
        self.bomb_img = pygame.image.load("bomb.png").convert_alpha()
        self.bomb_img = pygame.transform.scale(self.bomb_img, (21,21))

        self.flags = 0
        self.flag_list = []
        self.empty_list = []
        self.touching_list = []
        self.bomb_list = []
        self.board_list = []

        self.get_boardlist()

    def get_boardlist(self):
        """
        Makes a list of coordinates for each cell.
        """
        for a, x in enumerate(range(15, 785, 25)):
            for b, y in enumerate(range(90, 580, 25)):
                self.board_list.append([x,y])
        return self.board_list

    def board(self):
        """
        Draws pics based on Array.
        """
        for a, x in enumerate(range(15, 785, 25)):
            for b, y in enumerate(range(90, 580, 25)):
                if self.np_board.board[a][b] == 0:
                    pygame.draw.rect(self.screen, MS.WHITE, [x, y, 23,23], 0)
                    self.empty_list.append([x, y])
                elif self.np_board.board[a][b] > 0:
                    text = self.font_board.render(str(self.np_board.board[a][b]), True, (0, 128, 0))
                    pygame.draw.rect(self.screen, MS.WHITE, [x, y, 23,23], 0)
                    self.screen.blit(text, (x+5,y+2))
                    self.touching_list.append([x, y])
                elif self.np_board.board[a][b] == -1:
                    pygame.draw.rect(self.screen, MS.RED, [x, y, 23,23], 0)
                    self.screen.blit(self.bomb_img,(x+1, y+1))
                    self.bomb_list.append([x, y])
                # elif self.np_board.board[a][b] == -2:
                #     self.screen.blit(self.flag_img, [x, y])
                # elif [x, y] in self.flag_list:
                #     self.screen.blit(self.flag_img, [x, y])

    def cover(self):
        """
        Hides all the cells based on board_list (not clicked).
        """
        for xy in self.board_list:
            pygame.draw.rect(self.screen, MS.GREY, [xy[0], xy[1], 23,23], 0)
        for xy in self.flag_list:
            pygame.draw.rect(self.screen, MS.GREY, [xy[0], xy[1], 23,23], 0)
            self.screen.blit(self.flag_img, [xy[0], xy[1]])

    def clicked(self):
        """
        If clicked, cell removed from board_list. So it will be not covered.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = min(a[0] for a in self.board_list if abs(a[0]-pygame.mouse.get_pos()[0])<24)
                y = min(a[1] for a in self.board_list if abs(a[1]-pygame.mouse.get_pos()[1])<24)
                if [x, y] in self.board_list:
                    self.board_list.pop(self.board_list.index([x, y]))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                x = min(a[0] for a in self.board_list if abs(a[0]-pygame.mouse.get_pos()[0])<24)
                y = min(a[1] for a in self.board_list if abs(a[1]-pygame.mouse.get_pos()[1])<24)
                # Adding flags by updating flag_list
                if [x,y] in self.board_list:
                    self.board_list.pop(self.board_list.index([x,y]))
                    self.flag_list.append([x, y])
                    self.flags += 1
                # Removing flags from flag_list
                elif [x,y] not in self.board_list and [x, y] in self.flag_list:
                    self.board_list.append([x,y])
                    self.flag_list.pop(self.flag_list.index([x, y]))
                    self.flags -= 1

    def header(self, surface):
        move_counter = 620 % len(self.board_list)

        moves_text = self.font_header_value.render("620"+"/"+str(move_counter), True, (255, 0, 0))

        bombs_text = self.font_header_text.render("Bombs", True, (255, 0, 0))
        bombs_value = self.font_header_value.render(str(self.bomb_qty), True, (255, 0, 0))
        flags_text = self.font_header_text.render("Flags", True, (255, 0, 0))
        flags_value = self.font_header_value.render(str(self.flags), True, (255, 0, 0))

        surface.blit(moves_text, (650, 15))
        surface.blit(bombs_text, (20, 5))
        surface.blit(bombs_value, (20, 25))
        surface.blit(flags_text, (100, 5))
        surface.blit(flags_value, (100, 25))

    def game(self):
        clock = pygame.time.Clock()
        running = True
        top_screen = self.screen.subsurface(pygame.Rect(0, 0, 805, 80 ))
        while running:
            clock.tick(90)
            top_screen.fill((50, 20, 50))

            self.board()
            self.cover()
            self.clicked()

            self.header(top_screen)

            pygame.display.update()
        pygame.quit()


if __name__ == "__main__":
    minesweeper = MS()
    minesweeper.game()


