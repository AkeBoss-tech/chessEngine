import pygame, random, math, time, os

def drawRectangle(screen, color, x, y, width=100, height=100):
    pygame.draw.rect(screen, color, (x, y, width, height))

def drawHollowCircle(screen, color, radius, center_x, center_y):
    iterations = 100
    for i in range(iterations):
        ang = i * 3.14159 * 2 / iterations
        dx = int(math.cos(ang) * radius)
        dy = int(math.sin(ang) * radius)
        x = center_x + dx
        y = center_y + dy
        pygame.draw.circle(screen, color, (x, y), 5)

def drawCircle(screen, color, x, y, width, height):
    rect = [x, y, width, height]
    pygame.draw.ellipse(screen, color, rect, 0)

def writeText(text, screen, X, Y, color=(0, 0, 0), fontSize=64):
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', fontSize)

    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(text, True, color)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (X, Y)
    screen.blit(text, textRect)

class screen():
    def __init__(self):
        self.screenHeight = 950
        self.screenWidth = 950
        self.white = (255, 255, 255)
        self.black = (38, 38, 38)
        self.pureBlack = (1, 4, 105)
        self.gray = (166, 166, 166)
        self.red = (207, 0, 0)
        self.blue = (7, 219, 131)
        self.lightGreen = (210, 235, 52)
        self.green = (10, 186, 7)
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        path = os.path.dirname(os.path.realpath(__file__))
        path = path + r"\icons"
        self.wQ = pygame.image.load(str(path) + r"\wQ.png")
        self.wQ = pygame.transform.rotozoom(self.wQ, 0, 1.5)
        self.wK = pygame.image.load(str(path) + r"\wK.png")
        self.wK = pygame.transform.rotozoom(self.wK, 0, 1.5)
        self.wN = pygame.image.load(str(path) + r"\wN.png")
        self.wN = pygame.transform.rotozoom(self.wN, 0, 1.5)
        self.wR = pygame.image.load(str(path) + r"\wR.png")
        self.wR = pygame.transform.rotozoom(self.wR, 0, 1.5)
        self.wp = pygame.image.load(str(path) + r"\wp.png")
        self.wp = pygame.transform.rotozoom(self.wp, 0, 1.5)
        self.wB = pygame.image.load(str(path) + r"\wB.png")
        self.wB = pygame.transform.rotozoom(self.wB, 0, 1.5)
        self.bQ = pygame.image.load(str(path) + r"\bQ.png")
        self.bQ = pygame.transform.rotozoom(self.bQ, 0, 1.5)
        self.bK = pygame.image.load(str(path) + r"\bK.png")
        self.bK = pygame.transform.rotozoom(self.bK, 0, 1.5)
        self.bN = pygame.image.load(str(path) + r"\bN.png")
        self.bN = pygame.transform.rotozoom(self.bN, 0, 1.5)
        self.bR = pygame.image.load(str(path) + r"\bR.png")
        self.bR = pygame.transform.rotozoom(self.bR, 0, 1.5)
        self.bp = pygame.image.load(str(path) + r"\bp.png")
        self.bp = pygame.transform.rotozoom(self.bp, 0, 1.5)
        self.bB = pygame.image.load(str(path) + r"\bB.png")
        self.bB = pygame.transform.rotozoom(self.bB, 0, 1.5)
        pygame.display.set_caption('Chess Engine')

    def welcomeScreen(self):
        
        self.screen.fill(self.black)
        for i in range(15):
            drawCircle(self.screen, self.white, random.randint(0,950), random.randint(0,950), 5, 5)
            
        writeText("Checkers", self.screen, 450, 60, self.white)
        drawRectangle(self.screen, self.gray, 250, 350, 400, 150)
        drawRectangle(self.screen, self.gray, 250, 650, 400, 150)
        drawRectangle(self.screen, self.gray, 750, 0, 200, 100)
        
        writeText("View", self.screen, 455, 425, self.white)
        writeText("Play", self.screen, 455, 725, self.white)
        writeText("Help", self.screen, 850, 50, self.white)
        writeText("By: Akash Dubey", self.screen, 650, 900, self.white)
        

        pygame.display.update()

    def playScreen(self):
        self.screen.fill(self.black)
        for i in range(10):
            drawCircle(self.screen, self.white, random.randint(0,950), random.randint(0,950), 5, 5)
            
        writeText("Play", self.screen, 450, 60, self.white)
        drawRectangle(self.screen, self.gray, 250, 350, 400, 150)
        drawRectangle(self.screen, self.gray, 250, 750, 400, 100)
        drawRectangle(self.screen, self.gray, 250, 550, 400, 150)
        writeText("COMPUTER", self.screen, 455, 425, self.white)
        writeText("HUMAN", self.screen, 455, 625, self.white)
        writeText("BACK", self.screen, 455, 800, self.white)
        writeText("vs.", self.screen, 450, 200, self.white)

        pygame.display.update()

    def viewScreen(self, text, subText=""):
        self.screen.fill(self.black)
        for i in range(10):
            drawCircle(self.screen, self.white, random.randint(0,950), random.randint(0,950), 5, 5)
        
        writeText(text, self.screen, 455, 260, self.white)
        writeText(subText, self.screen, 450, 425, self.white)
        writeText("Click to advance", self.screen, 455, 625, self.white)

        pygame.display.update()

    def endScreen(self):
        self.screen.fill(self.black)
        for i in range(15):
            drawCircle(self.screen, self.white, random.randint(0,950), random.randint(0,950), 5, 5)
            
        writeText("Save the game?", self.screen, 450, 160, self.white)
        drawRectangle(self.screen, self.gray, 250, 350, 400, 150)
        drawRectangle(self.screen, self.gray, 250, 650, 400, 150)
        writeText("Yes", self.screen, 455, 425,self. white)
        writeText("No", self.screen, 455, 725, self.white)
        

        pygame.display.update()
    
    def chooseComputerScreen(self):
        self.screen.fill(self.black)
        for i in range(15):
            drawCircle(self.screen, self.white, random.randint(0,950), random.randint(0,950), 5, 5)
            
        writeText("Computer Menu", self.screen, 450, 60, self.white)
        drawRectangle(self.screen, self.gray, 50, 250, 400, 250) # Random
        drawRectangle(self.screen, self.gray, 500, 250, 400, 250) # Easy
        drawRectangle(self.screen, self.gray, 50, 550, 400, 250) # Medium
        drawRectangle(self.screen, self.gray, 500, 550, 400, 250) # Hard
        drawRectangle(self.screen, self.gray, 50, 825, 850, 100) # UNDO
        writeText("RANDOM", self.screen, 50+180, 250+130, self.white)
        writeText("EASY", self.screen, 500+185, 250+130, self.white)
        writeText("MEDIUM", self.screen, 250, 675, self.white)
        writeText("HARD", self.screen, 690, 675, self.white)
        writeText("BACK", self.screen, 455, 885, self.white)
        

        pygame.display.update()
    
    def confirmScreen(self, text, subText=""):
        self.screen.fill(self.black)
        for i in range(15):
            drawCircle(self.screen, self.white, random.randint(0,950), random.randint(0,950), 5, 5)
            
        writeText(text, self.screen, 450, 160, self.white)
        writeText(subText, self.screen, 450, 260, self.white)
        drawRectangle(self.screen, self.gray, 250, 350, 400, 150)
        drawRectangle(self.screen, self.gray, 250, 650, 400, 150)
        writeText("Yes", self.screen, 455, 425, self.white)
        writeText("No", self.screen, 455, 725,self.white)
        

        pygame.display.update()

    def drawGrid(self, board, highlightList):
        screen = self.screen
        screen.fill((162, 163, 162))
        colorsGrid = [
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1]
        ]
        drawRectangle(screen, self.green, 0, 0)
        white = (255, 255, 255)
        black = (125, 51, 2)
        gray = (166, 166, 166)
        red = (255, 0, 0)
        blue = (7, 219, 131)
        green = (10, 186, 7)
        bufferX = 0
        bufferY = 0
        for a, r in enumerate(colorsGrid):
            for b, c in enumerate(r):
                if c == 0:
                    drawRectangle(screen, black, bufferX + (b + 1) * 100, bufferY + (a + 1) * 100)
                elif c == 1:
                    drawRectangle(screen, white, bufferX + (b + 1) * 100, bufferY + (a + 1) * 100)

                for i in range(len(highlightList)):
                    if highlightList[i][0] == [int(a), int(b)]:
                        if highlightList[i][1] == "green":
                            drawHollowCircle(screen, green, 35, bufferX + (b + 1) * 100 + 50, bufferY + (a + 1) * 100 + 50)
                        elif highlightList[i][1] == "red":
                            drawRectangle(screen, red, bufferX + (b + 1) * 100, bufferY + (a + 1) * 100)
                        elif highlightList[i][1] == "blue":
                            drawRectangle(screen, blue, bufferX + (b + 1) * 100, bufferY + (a + 1) * 100)
                        elif highlightList[i][1] == "lightGreen":
                            drawRectangle(screen, self.lightGreen, bufferX + (b + 1) * 100, bufferY + (a + 1) * 100)
                        elif highlightList[i][1] == "darkGreen":
                            drawRectangle(screen, green, bufferX + (b + 1) * 100, bufferY + (a + 1) * 100)
                        elif highlightList[i][1] == "circle":
                            drawHollowCircle(screen, gray, 25, bufferX + (b + 1) * 100 + 50, bufferY + (a + 1) * 100 + 50)
                        elif highlightList[i][1] == "gray":
                            drawRectangle(screen, gray, bufferX + (b + 1) * 100, bufferY + (a + 1) * 100)

        bufferX += 1
        bufferY += 5
        for x, row in enumerate(board):
            for y, val in enumerate(row):
                if val != "--":
                    pieceVal = val.type
                    color = val.color

                    if color == "white":
                        if pieceVal == "Bishop":
                            screen.blit(self.wB, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Queen":
                            screen.blit(self.wQ, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "King":
                            screen.blit(self.wK, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Pawn":
                            screen.blit(self.wp, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Rook":
                            screen.blit(self.wR, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Knight":
                            screen.blit(self.wN, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))

                    elif color == "black":
                        if pieceVal == "Bishop":
                            screen.blit(self.bB, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Queen":
                            screen.blit(self.bQ, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "King":
                            screen.blit(self.bK, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Pawn":
                            screen.blit(self.bp, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Rook":
                            screen.blit(self.bR, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                        elif pieceVal == "Knight":
                            screen.blit(self.bN, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))

                    """for piece in pieces:
                        if piece in val:
                            pieceVal = val[:2]
                            if pieceVal == "wB":
                                screen.blit(wB, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "wQ":
                                screen.blit(wQ, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "wK":
                                screen.blit(wK, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "wp":
                                screen.blit(wp, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "wR":
                                screen.blit(wR, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "wN":
                                screen.blit(wN, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "bB":
                                screen.blit(bB, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "bQ":
                                screen.blit(bQ, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "bK":
                                screen.blit(bK, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "bp":
                                screen.blit(bp, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "bR":
                                screen.blit(bR, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))
                            elif pieceVal == "bN":
                                screen.blit(bN, (bufferX + (y + 1) * 100, bufferY + (x + 1) * 100))"""
        s = 150
        for a in range(8):
            writeText(str(a), screen, s + a * 100, 50)

        for b in range(8):
            writeText(str(b), screen, 50, s + b * 100)

        pygame.display.update()

