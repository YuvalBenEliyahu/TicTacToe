import pygame
pygame.init()

#Creating AppWindow
win = pygame.display.set_mode((300, 300))
pygame.display.set_caption("TicTacToe") # Title
bg = pygame.image.load('BG2.jpg') # BackGround


class Game():
    def __init__(self, x=-100, y=-100):
        self.turns = 0 # 0 X , 1  Circle
        self.x = x
        self.y = y
        self.widthX = 8
        self.widthCirc = 6
        self.widthWinLine = 6
        self.colorWinLine = (64, 64, 64)
        self.colorX = (84, 84, 84) # color of x
        self.colorCirc = (242, 235, 211)
        self.radius = 25
        self.game =  [[0,0,0],
                      [0,0,0],
                      [0,0,0],]
        self.turns = 0 # 0 For X turn || 1 For O Turn
        self.winline = 0 # explained inside DrawWinLine function
        self.winner = False # when True game pause
        self.Xwins = 0
        self.Owins = 0

    def Draw(self, win):
        if self.turns == 1 :
            if self.game[self.y // 100][self.x // 100] == 0:
                pygame.draw.circle(win, self.colorCirc, (self.x + 50,self.y + 50), self.radius, self.widthCirc)
                self.turns = 0
                self.game[self.y // 100][self.x // 100] = -1

        elif self.game[self.y // 100][self.x // 100] == 0:
            pygame.draw.line(win, self.colorX, (self.x+25, self.y+25), (self.x + 75, self.y + 75), self.widthX)
            pygame.draw.line(win, self.colorX, (self.x + 75, self.y+25), (self.x + 25, self.y + 75), self.widthX)
            self.turns = 1
            self.game[self.y // 100][self.x // 100] = 1

    def checkforwin(self):
        # Rows
        for i in range(3):
            if self.game[i][0] + self.game[i][1] + self.game[i][2] == 3:
                self.colorWinLine = self.colorX
                self.Xwins += 1
                Game.DrawWinLine(self, 1)
            elif self.game[i][0] + self.game[i][1] + self.game[i][2] == -3:
                self.colorWinLine = self.colorCirc
                self.Owins += 1
                Game.DrawWinLine(self, 1)
        # Columns
        for i in range(3):
            if self.game[0][i] + self.game[1][i] + self.game[2][i] == 3:
                self.colorWinLine = self.colorX
                self.Xwins += 1
                Game.DrawWinLine(self, 2)
            elif self.game[0][i] + self.game[1][i] + self.game[2][i] == -3:
                self.colorWinLine = self.colorCirc
                self.Owins += 1
                Game.DrawWinLine(self, 2)

        #Diagonal top left to bottom right
        if self.game[0][0] + self.game[1][1] + self.game[2][2] == 3:
            self.colorWinLine = self.colorX
            self.Xwins += 1
            Game.DrawWinLine(self, 3)
        if self.game[0][0] + self.game[1][1] + self.game[2][2] == -3:
            self.colorWinLine = self.colorCirc
            self.Owins += 1
            Game.DrawWinLine(self, 3)

        # Diagonal top right to bottom left
        if self.game[2][0] + self.game[1][1] + self.game[0][2] == 3:
            self.colorWinLine = self.colorX
            self.Xwins += 1
            Game.DrawWinLine(self, 4)
        if self.game[2][0] + self.game[1][1] + self.game[0][2] == -3:
            self.colorWinLine = self.colorCirc
            self.Owins += 1
            Game.DrawWinLine(self, 4)

    def DrawWinLine(self, i):
        # i: 1 for row, 2 for column, 3 for Diagonal left right, 4 Diagonal right left
        if i == 1:
            if self.y == 0:
                pygame.draw.line(win, self.colorWinLine, (25, 50), (275, 50), self.widthWinLine)
                self.winner = True
            elif self.y == 100:
                pygame.draw.line(win, self.colorWinLine, (25, 150), (275, 150), self.widthWinLine)
                self.winner = True
            elif self.y == 200:
                pygame.draw.line(win, self.colorWinLine, (25, 250), (275, 250), self.widthWinLine)
                self.winner = True

        if i == 2:
            if self.x == 0:
                pygame.draw.line(win, self.colorWinLine, (50, 25), (50, 275), self.widthWinLine)
                self.winner = True
            elif self.x == 100:
                pygame.draw.line(win, self.colorWinLine, (150, 25), (150, 275), self.widthWinLine)
                self.winner = True
            elif self.x == 200:
                pygame.draw.line(win, self.colorWinLine, (250, 25), (250, 275), self.widthWinLine)
                self.winner = True

        if i == 3:
            pygame.draw.line(win, self.colorWinLine, (25, 25), (275, 275), self.widthWinLine)
            self.winner = True
        if i == 4:
            pygame.draw.line(win, self.colorWinLine, (275, 25), (25, 275), self.widthWinLine)
            self.winner = True


def BackGroundDrew():
    win.blit(bg, (0, 0))  # Loading BackGround

    # Lines
    colorLine = (239, 239, 239)
    pygame.draw.line(win, colorLine, (20, 100), (280, 100), 6)
    pygame.draw.line(win, colorLine, (20, 200), (280, 200), 6)
    pygame.draw.line(win, colorLine, (100, 20), (100, 280), 6)
    pygame.draw.line(win, colorLine, (200, 20), (200, 280), 6)



def main(Owins = 0, Xwins = 0):
    BackGroundDrew()
    player = Game()
    run = True
    while run:
        pygame.time.delay(150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if not (player.winner):
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    player.x = pos[0] // 100 * 100
                    player.y = pos[1] // 100 * 100
                    player.Draw(win)
                    player.checkforwin()
            else:
                Owins += player.Owins
                Xwins += player.Xwins
                main(Owins,Xwins)

        pygame.display.update()

main()
pygame.quit()