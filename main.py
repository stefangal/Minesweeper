import pygame
from pygame.locals import *
from source import Array
import time


class MS:
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREY = (200,200,200)
    BLACK = (0, 0, 0)
    W = 805
    H = 600

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("M   I   N   E   S   W   E   E   P   E   R")
        self.w = self.W-30 # 775
        self.h = self.H-100 # 500
        self.offsetX = 5
        self.screen = pygame.display.set_mode((self.W, self.H))

        self.font_board = pygame.font.SysFont(None, 30)
        self.font_header_text = pygame.font.SysFont("Comic Sans MS", 16)
        self.font_header_value = pygame.font.SysFont("Comic Sans MS", 24)
        self.textE1 = "EASY"
        self.textE2 = "8x8"
        self.textM1 = "MEDIUM"
        self.textM2 = "16x16"
        self.textD1 = "EXPERT"
        self.textD2 = "24x24"
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
        self.restart_text = self.font_header_text.render("RESTART", True, (255, 255, 255))

        self.flag_img = pygame.image.load("img/flag.png").convert_alpha()
        self.flag_img = pygame.transform.scale(self.flag_img, (23,23))
        self.bomb_img = pygame.image.load("img/bomb.jpg").convert_alpha()
        self.bomb_img = pygame.transform.scale(self.bomb_img, (24,24))
        self.BOMB_img = pygame.image.load("img/bomb.jpg").convert_alpha()
        self.BOMB_img = pygame.transform.scale(self.BOMB_img, (200,200)) #1:1
        self.LOL_img = pygame.image.load("img/LOL.png").convert_alpha()
        self.LOL_img = pygame.transform.scale(self.LOL_img, (200,200))
        self.WON_img = pygame.image.load("img/WON.png").convert_alpha()
        self.WON_img = pygame.transform.scale(self.WON_img, (200,200))

        self.bang_img0 = pygame.image.load("explosion/regularExplosion00.png").convert_alpha()
        self.bang_img0 = pygame.transform.scale(self.bang_img0, (23,23))
        self.bang_img1 = pygame.image.load("explosion/regularExplosion01.png").convert_alpha()
        self.bang_img1 = pygame.transform.scale(self.bang_img1, (30,30))
        self.bang_img2 = pygame.image.load("explosion/regularExplosion02.png").convert_alpha()
        self.bang_img2 = pygame.transform.scale(self.bang_img2, (50,50))
        self.bang_img3 = pygame.image.load("explosion/regularExplosion03.png").convert_alpha()
        self.bang_img3 = pygame.transform.scale(self.bang_img3, (40,40))
        self.bang_img4 = pygame.image.load("explosion/regularExplosion04.png").convert_alpha()
        self.bang_img4 = pygame.transform.scale(self.bang_img4, (70,70))
        self.bang_img5 = pygame.image.load("explosion/regularExplosion05.png").convert_alpha()
        self.bang_img5 = pygame.transform.scale(self.bang_img5, (92,92))
        self.bang_img6 = pygame.image.load("explosion/regularExplosion06.png").convert_alpha()
        self.bang_img6 = pygame.transform.scale(self.bang_img6, (98,98))
        self.bang_img7 = pygame.image.load("explosion/regularExplosion07.png").convert_alpha()
        self.bang_img7 = pygame.transform.scale(self.bang_img7, (110,110))
        self.bang_img8 = pygame.image.load("explosion/regularExplosion07.png").convert_alpha()
        self.bang_img8 = pygame.transform.scale(self.bang_img8, (130,130))
        self.bangs_imgs = [self.bang_img0, self.bang_img1, self.bang_img2, self.bang_img3, self.bang_img4, self.bang_img5, self.bang_img6, self.bang_img7, self.bang_img8]
        self.icon_img = pygame.image.load("img/icon.jpg")
        self.icon_img = pygame.transform.scale(self.icon_img, (15, 15))
        self.restart_img = pygame.image.load("img/restart.png").convert_alpha()
        self.restart_img = pygame.transform.scale(self.restart_img, (35,35))

        pygame.display.set_icon(self.icon_img)

        self.restart = False
        self.show = True
        self.difficulty = None
        self.bomb_qty = 10
        self.flags = 0
        self.flag_list = []
        self.empty_list = []
        self.touching_list = []
        self.bomb_list = []
        self.board_list = []
        self.uncovered_list = []

# --------------------------------------------- INTRO PAGE ---------------------------------------------

    def intro_page(self):
        self.screen.fill((51,204,204))
        # MINESWEEPER text
        head = pygame.font.SysFont("Comic Sans MS", 48)
        gamename = head.render("M I N E S W E E P E R", True, (255, 255, 0))
        self.screen.blit(gamename, (self.W//2-gamename.get_rect().centerx, self.H//5-gamename.get_rect().centery))
        # BOARD DIFFICULTY
        self.screen.blit(self.txtE1_surface, (self.W/4-self.txtE1_surface.get_rect().centerx, 400))
        self.screen.blit(self.txtE2_surface, (self.W/4-self.txtE2_surface.get_rect().centerx, 435))
        self.screen.blit(self.txtM1_surface, (self.W/2-self.txtM1_surface.get_rect().centerx, 400))
        self.screen.blit(self.txtM2_surface, (self.W/2-self.txtM2_surface.get_rect().centerx, 435))
        self.screen.blit(self.txtD1_surface, (self.W/4*3-self.txtD1_surface.get_rect().centerx, 400))
        self.screen.blit(self.txtD2_surface, (self.W/4*3-self.txtD2_surface.get_rect().centerx, 435))
        self.screen.blit(self.author_surface, (self.W/2-self.author_surface.get_rect().centerx, 580))
        self.screen.blit(self.BOMB_img, (self.W/2-self.BOMB_img.get_rect().centerx, 170))
        # NUMBER OF MINES
        bomb_font = pygame.font.SysFont(None, 28)
        b1 = bomb_font.render("10", True, (0, 0, 0))
        b2 = bomb_font.render("40", True, (0, 0, 0))
        b3 = bomb_font.render("99", True, (0, 0, 0))
        self.screen.blit(b1, (self.W/4-self.bomb_img.get_rect().centerx-15, 462))
        self.screen.blit(self.bomb_img, (self.W/4-self.bomb_img.get_rect().centerx+15, 460))
        self.screen.blit(b2, (self.W/2-self.bomb_img.get_rect().centerx-15, 462))
        self.screen.blit(self.bomb_img, (self.W/2-self.bomb_img.get_rect().centerx+15, 460))
        self.screen.blit(b3, (self.W/4*3-self.bomb_img.get_rect().centerx-15, 462))
        self.screen.blit(self.bomb_img, (self.W/4*3-self.bomb_img.get_rect().centerx+15, 460))

    def intro_events(self):
        txtE1pos = self.txtE1_surface.get_rect(topleft=(self.W/4-self.txtE1_surface.get_rect().centerx, 400))
        txtM1pos = self.txtM1_surface.get_rect(topleft=(self.W/2-self.txtM1_surface.get_rect().centerx, 400))
        txtD1pos = self.txtD1_surface.get_rect(topleft=(self.W/4*3-self.txtD1_surface.get_rect().centerx, 400))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
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

    def intro(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            if self.difficulty in [0, 1, 2]:
                running = False
            self.intro_events()
            self.intro_page()
            pygame.display.update()
        return self.difficulty
# --------------------------------------------- INTRO PAGE (END) ---------------------------------------------
    def make_boardlist(self, width, hight):
        """
        Makes a list of coordinates for each cell.
        """
        self.cellrect_list, self.board_list = [], []

        for b, y in enumerate(range(90, hight+75, 25)):
            for a, x in enumerate(range(15, width, 25)): #w+15
                cell = pygame.draw.rect(self.screen, self.WHITE, [x, y, 23,23], 0)
                self.cellrect_list.append(cell)
                if [x, y] not in self.board_list:
                    self.board_list.append([x, y])
        return self.board_list

    def draw_board(self):
        """
        Draw the board based on np_board.board numpy array.
        """
        self.bomb_list, self.empty_list, self.touching_list = [], [], []

        for a, y in enumerate(range(90, self.h+75, 25)):
            for b, x in enumerate(range(15, self.w, 25)):

                pygame.draw.rect(self.screen, self.WHITE, [x, y, 23,23], 0)

                if self.np_board.board[a][b] == 0:
                    self.empty_list.append([x, y])

                elif self.np_board.board[a][b] > 0:
                    text = self.font_board.render(str(self.np_board.board[a][b]), True, (0, 128, 0))
                    self.screen.blit(text, (x+5,y+2))
                    self.touching_list.append([x, y])

                elif self.np_board.board[a][b] == -1:
                    self.screen.blit(self.bomb_img,(x, y))
                    self.bomb_list.append([x, y])

    def cell_hider(self, visible):
        """
        Hides all the cells based on board_list (not clicked).
        """
        if visible:
            for x, y in self.board_list:
                pygame.draw.rect(self.screen, self.GREY, [x, y, 23,23], 0)
            for x, y in self.flag_list:
                pygame.draw.rect(self.screen, self.GREY, [x, y, 23,23], 0)
                self.screen.blit(self.flag_img, [x, y])

    def clicked(self):
        """
        If clicked within playing cells, cell removed from board_list.
        """
        restart_pos = self.restart_img.get_rect(topleft=(self.w//2+15, 30))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_pos.collidepoint(pygame.mouse.get_pos()):
                    return True
                else:
                    for cell in self.cellrect_list:

                        if cell.collidepoint(pygame.mouse.get_pos()):
                            x = cell.x
                            y = cell.y
                            if [x, y] in self.board_list:
                                removed = self.board_list.pop(self.board_list.index([x, y])) # remove from Board_list
                                self.uncovered_list.append(removed) # add to Uncovered list

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                 for cell in self.cellrect_list:
                    if cell.collidepoint(pygame.mouse.get_pos()):
                        x = cell.x
                        y = cell.y
                        # ADD FLAG by updating flag_list
                        if [x,y] in self.board_list:
                            removed = self.board_list.pop(self.board_list.index([x,y]))  # remove from Board_list
                            self.uncovered_list.append(removed)
                            self.flag_list.append([x, y])
                            self.flags += 1
                        # REMOVE FLAG from flag_list
                        elif [x,y] not in self.board_list and [x, y] in self.flag_list:
                            self.board_list.append([x,y])  # add to Board_list
                            self.flag_list.pop(self.flag_list.index([x, y])) # remove from Flag list
                            self.flags -= 1
            if self.restart:
                self.restart = False
                self.game()
        return False

    def header(self, surface):
        move_counter = len(self.uncovered_list)
        moves_text = self.font_header_value.render(str(move_counter)+"/"+str(self.np_board.board.size), True, (255, 0, 0))
        bombs_text = self.font_header_text.render("Bombs", True, (255, 0, 0))
        bombs_value = self.font_header_value.render(str(self.bomb_qty), True, (255, 0, 0))
        flags_text = self.font_header_text.render("Flags", True, (255, 0, 0))
        flags_value = self.font_header_value.render(str(self.flags), True, (255, 0, 0))

        surface.blit(moves_text, (self.w-(moves_text.get_rect().right), 5))
        surface.blit(bombs_text, (20, 5))
        surface.blit(bombs_value, (20, 25))
        surface.blit(flags_text, (80, 5))
        surface.blit(flags_value, (80, 25))

        surface.blit(self.restart_img, (surface.get_rect().centerx, self.offsetX+27))
        surface.blit(self.restart_text, (surface.get_rect().centerx-self.restart_text.get_rect().centerx+15, 65))

    def lost(self):
        for coord in self.bomb_list:
            if coord not in self.board_list and coord not in self.flag_list:
                return True
        return False

    def win_check(self):
        if sorted(self.bomb_list) == sorted(self.flag_list) and self.flag_list != [] and self.board_list == []:
            return True
        return False

    def game(self):
        clock = pygame.time.Clock()

        if self.difficulty == 0:
            self.bomb_qty, self.w, self.h = 10, 200, 200
        elif self.difficulty == 1:
            self.bomb_qty, self.w, self.h = 40, 400, 400
        elif self.difficulty == 2:
            self.bomb_qty, self.w, self.h = 99, 600, 600

        self.make_boardlist(self.w, self.h)

        self.screen = pygame.display.set_mode((self.w+30, self.h+100))
        top_screen = self.screen.subsurface(pygame.Rect(0, 0, self.w+30, 90))

        self.np_board = Array(self.w//25, self.h//25, self.bomb_qty)
        print(self.np_board.board)
        start_time = time.time()
        seconds, minutes = 0, 0

        once = 0

        running = True

        while running:
            clock.tick(60)


            # WHEN LOST --------------------------------------
            if self.lost():
                self.show = False # UNCOVER everything
                while not self.clicked():
                    once += 1
                    self.draw_board()

                    if once == 1:
                        for w, bang in enumerate(self.bangs_imgs):
                            x1, y1 = self.uncovered_list[-1]
                            pygame.time.wait(200*(1+w//100))
                            self.screen.blit(bang, (x1-3, y1-3))
                            pygame.display.update()

                    self.screen.blit(self.bang_img2, (x1-5, y1-5))
                    self.screen.blit(self.LOL_img, (top_screen.get_rect().centerx-100, top_screen.get_rect().centery+45))
                    top_screen.blit(timing, (self.w-(timing.get_rect().right), 40))

                    self.cell_hider(self.show)

                    if self.clicked():
                        running = False
                        break
                    pygame.display.update()

            # WHEN WON --------------------------------------
            if self.win_check():
                self.show = False
                while not self.clicked():
                    self.draw_board()
                    self.screen.blit(self.WON_img, (top_screen.get_rect().centerx-100, top_screen.get_rect().centery+45))

                    if self.clicked():
                        running = False
                        break
                    pygame.display.update()

            # IF WANT TO RESTART -------------------------------
            if self.clicked():
                running = False
                self.restart = True

            #TIMER --------------------------------
            if seconds > 60:
                minutes += 1
                seconds = 0
                start_time = time.time()
            else:
                seconds = (time.time() - start_time)

            # NORMAL GAME LOOP -------------------------------
            top_screen.fill((20, 20, 20))
            self.draw_board()

            timing = self.font_header_text.render(str(minutes).zfill(2)+":"+str(int(seconds)).zfill(2), True, (0,255,0))
            top_screen.blit(timing, (self.w-(timing.get_rect().right), 40))

            self.header(top_screen)
            self.cell_hider(self.show) # unhide cell with are not in board_list
            self.clicked() # remove clicked cell from board_list

            pygame.display.update()


if __name__ == "__main__":
    while True:
        minesweeper = MS()
        minesweeper.intro()
        minesweeper.game()
    pygame.quit()


