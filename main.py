# TODO
    #Sort out np_board class method !!!
import pygame
from pygame.locals import *
from source import Array

class MS:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (200,200,200)
    W = 805
    H = 600

    pygame.display.set_caption("M   I   N   E   S   W   E   E   P   E   R")


    def __init__(self):

        pygame.init()
        self.w = MS.W-30 # 775
        self.h = MS.H-100 # 500
        self.screen = pygame.display.set_mode((MS.W, MS.H))

        self.font_board = pygame.font.SysFont(None, 30)
        self.font_header_text = pygame.font.SysFont("Comic Sans MS", 20)
        self.font_header_value = pygame.font.SysFont("Comic Sans MS", 36)
        self.textE1 = "EASY"
        self.textE2 = "15x15"
        self.textM1 = "MEDIUM"
        self.textM2 = "25x25"
        self.textD1 = "DIFFICULT"
        self.textD2 = "35x35"
        self.author = "Copyright 2019 Stefan Gal"
        self.FONT1 = pygame.font.Font(None, 42)
        self.FONT2 = pygame.font.Font(None, 32)
        self.FONT3 = pygame.font.Font(None, 12)
        self.txtE1_surface = self.FONT1.render(self.textE1, True, (255, 0, 0))
        self.txtE2_surface = self.FONT2.render(self.textE2, True, (205, 255, 255))
        self.txtM1_surface = self.FONT1.render(self.textM1, True, (255, 0, 0))
        self.txtM2_surface = self.FONT2.render(self.textM2, True, (205, 255, 255))
        self.txtD1_surface = self.FONT1.render(self.textD1, True, (255, 0, 0))
        self.txtD2_surface = self.FONT2.render(self.textD2, True, (205, 255, 255))
        self.author_surface = self.FONT3.render(self.author, True, (255, 255, 255))

        self.flag_img = pygame.image.load("img/flag.png").convert_alpha()
        self.flag_img = pygame.transform.scale(self.flag_img, (23,23))
        self.bomb_img = pygame.image.load("img/bomb.png").convert_alpha()
        self.bomb_img = pygame.transform.scale(self.bomb_img, (21,21))
        self.BOMB_img = pygame.image.load("img/bomb.png").convert_alpha()
        self.BOMB_img = pygame.transform.scale(self.BOMB_img, (80,100)) #1: 1.2
        self.icon_img = pygame.image.load("img/icon.png")
        self.icon_img = pygame.transform.scale(self.icon_img, (15, 15))
        pygame.display.set_icon(self.icon_img)

        self.difficulty = None
        self.bomb_qty = 10
        self.flags = 0
        self.flag_list = []
        self.empty_list = []
        self.touching_list = []
        self.bomb_list = []
        self.board_list = []

        self.get_boardlist()


    def introPage(self):
        self.screen.fill((55,55,0))
        # MINESWEEPER text
        head = pygame.font.SysFont("Comic Sans MS", 48)
        gamename = head.render("M I N E S W E E P E R", True, (255, 255, 0))
        x = gamename.get_rect().centerx
        y = gamename.get_rect().centery
        self.screen.blit(gamename, (MS.W//2-x, MS.H//5-y))
        # BOARD DIFFICULTY
        self.screen.blit(self.txtE1_surface, (150,400))
        self.screen.blit(self.txtE2_surface, (155,435))
        self.screen.blit(self.txtM1_surface, (320,400))
        self.screen.blit(self.txtM2_surface, (345,435))
        self.screen.blit(self.txtD1_surface, (500,400))
        self.screen.blit(self.txtD2_surface, (535,435))
        self.screen.blit(self.author_surface, (335,580))
        self.screen.blit(self.BOMB_img, (350, 200))

    def events(self):
        txtE1pos = self.txtE1_surface.get_rect(topleft=(150, 400))
        txtM1pos = self.txtM1_surface.get_rect(topleft=(320, 400))
        txtD1pos = self.txtD1_surface.get_rect(topleft=(500, 400))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == QUIT:
                pygame.quit()

            if txtE1pos.collidepoint(pygame.mouse.get_pos()):
                self.txtE1_surface = self.FONT1.render(self.textE1, True, (0, 255, 0))
                if pygame.mouse.get_pressed()[0]:
                    self.difficulty = 0
                    return self.difficulty
            elif txtM1pos.collidepoint(pygame.mouse.get_pos()):
                self.txtM1_surface = self.FONT1.render(self.textM1, True, (0, 255, 0))
                if pygame.mouse.get_pressed()[0]:
                    self.difficulty = 1
                    return self.difficulty
            elif txtD1pos.collidepoint(pygame.mouse.get_pos()):
                self.txtD1_surface = self.FONT1.render(self.textD1, True, (0, 255, 0))
                if pygame.mouse.get_pressed()[0]:
                    self.difficulty = 2
                    return self.difficulty
            else:
                self.txtE1_surface = self.FONT1.render(self.textE1, True, (255, 0, 0))
                self.txtM1_surface = self.FONT1.render(self.textM1, True, (255, 0, 0))
                self.txtD1_surface = self.FONT1.render(self.textD1, True, (255, 0, 0))

    def get_boardlist(self):
        """
        Makes a list of coordinates for each cell.
        """
        for a, x in enumerate(range(15, self.w+15, 25)):
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

    def intro(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            if self.difficulty in [0,1,2]:
                running = False
                print(self.difficulty)
                return self.difficulty
            else:
                self.events()

            self.introPage()

            pygame.display.update()

        pygame.quit()


    def game(self, difficulty):
        clock = pygame.time.Clock()
        running = True
        self.screen.fill((0,0,0))
        top_screen = self.screen.subsurface(pygame.Rect(0, 0, 805, 80 ))
        if difficulty == 0:
            self.bomb_qty = 10
        elif difficulty == 1:
            self.bomb_qty = 20
        elif difficulty == 2:
            self.bomb_qty = 30

        self.np_board = Array(31, 20, self.bomb_qty)

        print(self.np_board)
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
    minesweeper.intro()

    minesweeper.game(minesweeper.difficulty)



