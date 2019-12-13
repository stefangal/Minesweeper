# TODO
    #clean the code
    #add action when win - when all bombs are flagged and rest is removed
    #(boardlist contains only flaglist and flaglist == bomblist)
    # add cell unocvered list. if game over, last item in uncovered list should be red. or add animation of blow up.

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
        self.uncovered = []

        #self.get_boardlist(self.w, self.h)


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

    def events(self):
        txtE1pos = self.txtE1_surface.get_rect(topleft=(self.W/4-self.txtE1_surface.get_rect().centerx, 400))
        txtM1pos = self.txtM1_surface.get_rect(topleft=(self.W/2-self.txtM1_surface.get_rect().centerx, 400))
        txtD1pos = self.txtD1_surface.get_rect(topleft=(self.W/4*3-self.txtD1_surface.get_rect().centerx, 400))

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

    def get_boardlist(self, width, hight):
        """
        Makes a list of coordinates for each cell.
        """

        self.cellrect_list, self.board_list = [], []
        # for a, x in enumerate(range(15, width, 25)): #w+15
        #     for b, y in enumerate(range(90, hight+75, 25)):
        for b, y in enumerate(range(90, hight+75, 25)):
            for a, x in enumerate(range(15, width, 25)): #w+15
                cell = pygame.draw.rect(self.screen, self.WHITE, [x, y, 23,23], 0)
                self.cellrect_list.append([cell])
                if [x, y] not in self.board_list:
                    self.board_list.append([x, y])
        print(self.cellrect_list)

        return self.board_list

    def board(self):
        """
        Draws pics based on Array.
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



    def cover(self, visible):
        """
        Hides all the cells based on board_list (not clicked).
        """
        if visible:
            for xy in self.board_list:
                pygame.draw.rect(self.screen, self.GREY, [xy[0], xy[1], 23,23], 0)
            for xy in self.flag_list:
                pygame.draw.rect(self.screen, self.GREY, [xy[0], xy[1], 23,23], 0)
                self.screen.blit(self.flag_img, [xy[0], xy[1]])

    def clicked(self):
        """
        If clicked within playing cells, cell removed from board_list.
        """

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if len(self.board_list) > 1:
                    #print(self.board_list)
                    if 15 < pygame.mouse.get_pos()[0] < self.w + 15 and 90 < pygame.mouse.get_pos()[1] < self.h + 88:
                        x = min(a[0] for a in self.board_list if abs(a[0]-pygame.mouse.get_pos()[0])<24)
                        y = min(b[1] for b in self.board_list if abs(b[1]-pygame.mouse.get_pos()[1])<24)
                        if [x, y] in self.board_list:
                            print(x, y)
                            removed = self.board_list.pop(self.board_list.index([x, y]))
                            self.uncovered.append(removed)

                elif len(self.board_list) == 1:
                    if 15 < pygame.mouse.get_pos()[0] < self.w + 10 and 90 < pygame.mouse.get_pos()[1] < self.h + 88:
                        x = self.board_list[0][0]
                        y = self.board_list[0][1]
                        if abs(x- pygame.mouse.get_pos()[0] < 24) and abs(y -pygame.mouse.get_pos()[1] < 24):
                            if [x, y] in self.board_list:
                                removed = self.board_list.pop(self.board_list.index([x, y]))
                                self.uncovered.append(removed)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                if len(self.board_list) > 1:
                    if  15 < pygame.mouse.get_pos()[0] < self.w + 15 and 90 < pygame.mouse.get_pos()[1] < self.h + 88:
                        x = min(a[0] for a in self.board_list if abs(a[0]-pygame.mouse.get_pos()[0])<24)
                        y = min(a[1] for a in self.board_list if abs(a[1]-pygame.mouse.get_pos()[1])<24)
                        # Adding flags by updating flag_list
                        if [x,y] in self.board_list:
                            removed = self.board_list.pop(self.board_list.index([x,y]))
                            self.uncovered.append(removed)
                            self.flag_list.append([x, y])
                            self.flags += 1
                        # Removing flags from flag_list
                        elif [x,y] not in self.board_list and [x, y] in self.flag_list:
                            self.board_list.append([x,y])
                            self.flag_list.pop(self.flag_list.index([x, y]))
                            self.flags -= 1
                elif len(self.board_list) == 1:
                    if  15 < pygame.mouse.get_pos()[0] < self.w + 10 and 90 < pygame.mouse.get_pos()[1] < self.h + 88:
                        x = self.board_list[0][0]
                        y = self.board_list[0][1]
                        if abs(x- pygame.mouse.get_pos()[0] < 24) and abs(y -pygame.mouse.get_pos()[1] < 24):
                          # Adding flags by updating flag_list
                            if [x,y] in self.board_list:
                                removed = self.board_list.pop(self.board_list.index([x,y]))
                                self.uncovered.append(removed)
                                self.flag_list.append([x, y])
                                self.flags += 1
                            # Removing flags from flag_list
                            elif [x,y] not in self.board_list and [x, y] in self.flag_list:
                                self.board_list.append([x,y])
                                self.flag_list.pop(self.flag_list.index([x, y]))
                                self.flags -= 1

    def restart_game(self, surface):
        restart_pos = self.restart_img.get_rect(topleft=(surface.get_rect().centerx-5, 35))

        for event in pygame.event.get():
            if restart_pos.collidepoint(pygame.mouse.get_pos()):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.offsetX = 10
                if event.type == pygame.MOUSEBUTTONUP:
                    self.offsetX = 5
                    self.restart = True
        return self.restart

    def header(self, surface):
        if self.show and self.board_list != []:
            move_counter = (self.w//25 * self.h//25) % len(self.board_list)
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
        else:
            surface.blit(self.restart_img, (surface.get_rect().centerx, self.offsetX+27))
            surface.blit(self.restart_text, (surface.get_rect().centerx-self.restart_text.get_rect().centerx+15, 65))

    def intro(self):
        clock1 = pygame.time.Clock()
        running = True
        while running:
            clock1.tick(60)
            if self.difficulty in [0,1,2]:
                running = False
            else:
                self.events()

            self.intro_page()
            pygame.display.update()
        return self.difficulty

    def lost_check(self):
        for koord in self.bomb_list:
            if koord not in self.board_list and koord not in self.flag_list:
                return True
            return False

    def win_check(self):
        if sorted(self.bomb_list) == sorted(self.flag_list) and self.flag_list != [] and self.board_list == []:
            print("WINNER")
            return True

    def game(self, difficulty):
        clock2 = pygame.time.Clock()
        running = True
        if difficulty == 0:
            self.bomb_qty, self.w, self.h = 10, 200, 200

        elif difficulty == 1:
            self.bomb_qty, self.w, self.h = 40, 400, 400

        elif difficulty == 2:
            self.bomb_qty, self.w, self.h = 99, 600, 600

        self.get_boardlist(self.w, self.h)

        self.screen = pygame.display.set_mode((self.w+30, self.h+100))
        self.screen.fill(self.BLACK)
        top_screen = self.screen.subsurface(pygame.Rect(0, 0, self.w+30, 88 ))
        self.np_board = Array(self.w//25, self.h//25, self.bomb_qty)

        start_time = time.time()

        minutes = 0
        once = 0
        print(self.np_board.board)
        while running:
            clock2.tick(60)
            #TIMER --------------------------------
            seconds = (time.time() - start_time)
            if (time.time() - start_time) > 59 == 0:
                minutes += 1
                start_time = time.time()
            #--------------------------------------
            if self.lost_check():
                self.show = False
                if self.restart_game(top_screen):
                    break
                else:
                    once += 1
                    self.board()
                    self.cover(self.show)
                    if once == 1:
                        for w, bang in enumerate(self.bangs_imgs):
                            x1, y1 = self.uncovered[-1]
                            pygame.time.wait(200*(1+w//100))
                            self.screen.blit(bang, (x1-3, y1-3))
                            pygame.display.flip()
                        pygame.draw.rect(self.screen, self.WHITE, [x1, y1, 23,23], 0)
                    self.screen.blit(self.bang_img2, (x1-5, y1-5))
                    self.screen.blit(self.LOL_img, (top_screen.get_rect().centerx-100, top_screen.get_rect().centery+45))
                    top_screen.blit(timing, (self.w-(timing.get_rect().right), 40))
                    self.clicked()
                    pygame.display.update()
            elif self.win_check():
                self.show = False
                if self.restart_game(top_screen):
                    break
                else:
                    self.board()
                    self.cover(self.show)
                    self.screen.blit(self.WON_img, (top_screen.get_rect().centerx-100, top_screen.get_rect().centery+45))

                    pygame.display.update()
            else:
                top_screen.fill((20, 20, 20))
                self.board()
                self.clicked()
                #self.cover(self.show)
                self.cover(False)

                if self.restart_game(top_screen):
                    break

                self.header(top_screen)


                timing = self.font_header_text.render(str(minutes).zfill(2)+":"+str(int(seconds)).zfill(2), True, (0,255,0))
                top_screen.blit(timing, (self.w-(timing.get_rect().right), 40))
                pygame.display.update()


if __name__ == "__main__":
    while True:
        minesweeper = MS()
        minesweeper.intro()
        minesweeper.game(minesweeper.difficulty)
    pygame.quit()


