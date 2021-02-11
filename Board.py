from Pieces import *

from copy import deepcopy
import os
import pygame

class game():
    def __init__(self):
        path = os.path.dirname(os.path.realpath(__file__))
        path = path + r"\sound\nes"
        self.capture_sound = pygame.mixer.Sound(str(path) + r"\Berserk.ogg")
        self.move_sound = pygame.mixer.Sound(str(path) + r"\Move.ogg")
        self.castle_sound = pygame.mixer.Sound(str(path) + r"\NewPM.ogg")
        self.check_sound = pygame.mixer.Sound(str(path) + r"\Check.ogg")
        self.board = [
            [Rook(0, 0, "black", 1), Knight(0, 1, "black", 1), Bishop(0, 2, "black", 1), Queen(0, 3, "black", 1),
             King(0, 4, "black"), Bishop(0, 5, "black", 2), Knight(0, 6, "black", 2), Rook(0, 7, "black", 2)],
            [Pawn(1, 0, "black", 1), Pawn(1, 1, "black", 2), Pawn(1, 2, "black", 3), Pawn(1, 3, "black", 4),
             Pawn(1, 4, "black", 5), Pawn(1, 5, "black", 6), Pawn(1, 6, "black", 7), Pawn(1, 7, "black", 8)],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            [Pawn(6, 0, "white", 1), Pawn(6, 1, "white", 2), Pawn(6, 2, "white", 3), Pawn(6, 3, "white", 4),
             Pawn(6, 4, "white", 5), Pawn(6, 5, "white", 6), Pawn(6, 6, "white", 7), Pawn(6, 7, "white", 8)],
            [Rook(7, 0, "white", 1), Knight(7, 1, "white", 1), Bishop(7, 2, "white", 1), Queen(7, 3, "white", 1),
             King(7, 4, "white"), Bishop(7, 5, "white", 2), Knight(7, 6, "white", 2), Rook(7, 7, "white", 2)]
        ]

        self.highlightedPieces = []
        self.takenPieces = []
        self.checkingPiece = []
        self.checkPath = []
        self.pinnedPieces = []
        self.colors = ["white", "black"]
        self.previousMoves = []
        self.turn = "white"
        self.screenHeight = 950
        self.screenWidth = 950
        self.boardType = "REAL"

    def returnOtherColor(self, color):
        if color in self.colors:
            index = self.colors.index(color)
            if index == 0:
                return self.colors[1]
            elif index == 1:
                return self.colors[0]
        raise Exception(f"Incorrect Input to Function returnOtherColor({color})")

    def changeTurn(self):
        self.turn = self.returnOtherColor(self.turn)
        self.clearHighlightedPieces()
        self.refreshGame()
        if self.getCheck(self.turn):
            self.check_sound.play()

    def changeHighlightedPieces(self, pos, color):
        self.highlightedPieces.append([list(pos), color])

    def clearHighlightedPieces(self):
        self.highlightedPieces = []

    def movePiece(self, row, col, newRow, newCol):
        x = self.board[row][col]
        y = self.board[newRow][newCol]

        if x.type == "King":
            if x.specialMove:
                for i in x.specialMove:
                    if i[0] == [newRow, newCol]:
                        self.board[newRow][newCol]      = x
                        self.board[row][col]            = "--"
                        self.previousMoves.append([[row, col], [newRow, newCol]])
                        self.board[newRow][newCol].changePos([newRow, newCol])
                        y = self.board[i[1][0]][i[1][1]]
                        self.board[i[2][0]][i[2][1]] = y
                        self.board[i[1][0]][i[1][1]] = "--"
                        self.board[i[2][0]][i[2][1]].changePos([i[2][0], i[2][1]])
                        self.board[newRow][newCol].checkAttackingPieces(self)
                        self.board[i[2][0]][i[2][1]].checkAttackingPieces(self)
                        if self.boardType == "REAL":
                            self.castle_sound.play()
                        return
                        

        if y != "--":
            if x.color is y.color:
                print("cant take")
                raise Exception("Can not take piece")
            elif x.color is not y.color:
                self.board[newRow][newCol] = x
                self.board[row][col] = "--"
                self.takenPieces.append(y)
                self.board[newRow][newCol].changePos([newRow, newCol])
                self.previousMoves.append([[row, col], [newRow, newCol]])
                if self.boardType == "REAL":
                    self.capture_sound.play()
        else:
            self.board[newRow][newCol] = x
            self.board[row][col] = "--"
            self.board[newRow][newCol].changePos([newRow, newCol])
            self.previousMoves.append([[row, col], [newRow, newCol]])
            if self.boardType == "REAL":
                self.move_sound.play()
        
        self.board[newRow][newCol].checkAttackingPieces(self)

    def undoMove(self):
        self.board = simulateGame(self.previousMoves[:-1]).board
        self.turn = self.returnOtherColor(self.turn)
        self.previousMoves = self.previousMoves[:-1]
        self.refreshGame()

    def returnBoard(self):
        return self.board

    def getPiece(self, position):
        return self.board[position[0]][position[1]]

    def replacePiece(self, position, newVal):
        self.board[position[0]][position[1]] = newVal

    def isPiece(self, position, piece=False):
        if piece:
            return True if position != "--" else False

        return True if self.getPiece(position) != "--" else False

    def refreshGame(self):
        for row in self.board:
            for piece in row:
                if self.isPiece(piece, True):
                    piece.checkAttackingPieces(self)
                    if piece.type == "Pawn" and piece.color == "white" and self.board.index(row) == 0:
                        self.promotePawn(self.getArrayPos(piece))
                    elif piece.type == "Pawn" and piece.color == "black" and self.board.index(row) == 7:
                        self.promotePawn(self.getArrayPos(piece))

        self.getCheck(self.turn)

    def getArrayPos(self, piece):
        for row in self.board:
            if piece in row:
                pieceCol = row.index(piece)
                pieceRow = self.board.index(row)
                return [pieceRow, pieceCol]
        
        raise Exception(f"Piece not on Board getArrayPos({piece})")

    def getCheck(self, color):
        canMove = []
        for r in self.board:
            for piece in r:
                if self.isPiece(piece, True):
                    if piece.type == "King" and piece.color == color:
                        row = self.board.index(r)
                        col = r.index(piece)
        
        canMove.append(checkForCheckDiagonal(row, col, 1, 0, color, self, ["Rook", "Queen"])[0])
        canMove.append(checkForCheckDiagonal(row, col, -1, 0, color, self, ["Rook", "Queen"])[0])
        canMove.append(checkForCheckDiagonal(row, col, 0, -1, color, self, ["Rook", "Queen"])[0])
        canMove.append(checkForCheckDiagonal(row, col, 0, 1, color, self, ["Rook", "Queen"])[0])
        canMove.append(checkForCheckDiagonal(row, col, 1, 1, color, self, ["Bishop", "Queen"])[0])
        canMove.append(checkForCheckDiagonal(row, col, 1, -1, color, self, ["Bishop", "Queen"])[0])
        canMove.append(checkForCheckDiagonal(row, col, -1, 1, color, self, ["Bishop", "Queen"])[0])
        canMove.append(checkForCheckDiagonal(row, col, -1, -1, color, self, ["Bishop", "Queen"])[0])

        if not checkForCheckAroundKing(row, col, self, color):
            canMove.append(False)
        else:
            canMove.append(True)

        if True in canMove:
            print("CHECK")
            return True

        return False

    def getPaths(self, color):
        self.checkingPiece = []
        self.checkPath = []
        check = []
        for r in self.board:
            for piece in r:
                if self.isPiece(piece, True):
                    if piece.type == "King" and piece.color == color:
                        row = self.board.index(r)
                        col = r.index(piece)
        
        check.append(checkForCheckDiagonal(row, col, 1, 0, color, self, ["Rook", "Queen"]))
        check.append(checkForCheckDiagonal(row, col, -1, 0, color, self, ["Rook", "Queen"]))
        check.append(checkForCheckDiagonal(row, col, 0, -1, color, self, ["Rook", "Queen"]))
        check.append(checkForCheckDiagonal(row, col, 0, 1, color, self, ["Rook", "Queen"]))
        check.append(checkForCheckDiagonal(row, col, 1, 1, color, self, ["Bishop", "Queen"]))
        check.append(checkForCheckDiagonal(row, col, 1, -1, color, self, ["Bishop", "Queen"]))
        check.append(checkForCheckDiagonal(row, col, -1, 1, color, self, ["Bishop", "Queen"]))
        check.append(checkForCheckDiagonal(row, col, -1, -1, color, self, ["Bishop", "Queen"]))

        for diagonal in check:
            if diagonal[0]:
                self.checkingPiece.append(diagonal[1])
                for item in diagonal[2]:
                    self.checkPath.append(item)

        checks = checkForCheckAroundKing(row, col, self, color)
        if checks:
            for item in checks:
                self.checkingPiece.append(item)

    def getPin(self, color):
        self.pinnedPieces = []
        King = None
        for row in self.board:
            for piece in row:
                if self.isPiece(piece, True):
                    if piece.type == "King" and piece.color == color:
                        King = piece
                        break
        
        row = self.getArrayPos(King)[0]
        col = self.getArrayPos(King)[1]
        
        checkForPin(row, col, 1, 0, color, self, ["Rook", "Queen"])
        checkForPin(row, col, -1, 0, color, self, ["Rook", "Queen"])
        checkForPin(row, col, 0, -1, color, self, ["Rook", "Queen"])
        checkForPin(row, col, 0, 1, color, self, ["Rook", "Queen"])
        checkForPin(row, col, 1, 1, color, self, ["Bishop", "Queen"])
        checkForPin(row, col, -1, -1, color, self, ["Bishop", "Queen"])
        checkForPin(row, col, 1, -1, color, self, ["Bishop", "Queen"])
        checkForPin(row, col, -1, 1, color, self, ["Bishop", "Queen"])

    def getKing(self, color):
        for r in self.board:
            for piece in r:
                if self.isPiece(piece, True):
                    if piece.type == "King" and piece.color == color:
                        return [self.board.index(r), r.index(piece)]

    def getLegalMoves(self, position):
        positions = []
        piece = self.getPiece(position)
        positions = piece.checkAttackingPieces(self)
        self.getPin(piece.color)
        if position in self.pinnedPieces:
            positions = []

        if self.getCheck(self.turn):
            self.getPaths(self.turn)
            if len(self.checkingPiece) != 1:
                if position != self.getKing(self.turn):
                    positions = []
                
            elif len(self.checkingPiece) == 1:
                if position != self.getKing(self.turn):
                    possibleBlockPos = []
                    possibleBlockPos.append(self.checkingPiece[0])
                    for item in self.checkPath:
                        possibleBlockPos.append(item)
                    
                    deletePositions = []
                    for pos in positions:
                        if not pos in possibleBlockPos:
                            deletePositions.append(pos)
                    
                    for delete in deletePositions:
                        positions.remove(delete)

        return positions
        
    def checkIfPossibleOnBoard(self, position):
        onBoard = False
        if 0 <= position[0] < 8 and 0 <= position[1] < 8:
            onBoard = True

        return onBoard

    def Threatened(self, position, color=False):
        piece = self.getPiece(position)
        if color:
            friendlyColor = color
        else:
            piece = self.getPiece(position)
            friendlyColor = piece.color

        enemySquares = []
        for row in self.board:
            for x in row:
                if self.isPiece(x, True) and x.color != friendlyColor:
                    x.checkAttackingPieces(self, False)
                    for attacked in x.attackingEnemy:
                        if position is attacked:
                            return True


        if position in enemySquares:
            return True
        
        return False
    
    def canKingMove(self, position, friendlyColor):
        """
        enemySquares = []
        for row in self.board:
            for x in row:
                if self.isPiece(x, True) and x.color != friendlyColor:
                    for attacked in x.controllingSquares:
                        if attacked:
                            enemySquares.append(attacked)
        if position in enemySquares:
            return True
        
        return False
        checkForPin(row, col, 1, 0, color, self, ["Rook", "Queen"])
        checkForPin(row, col, -1, 0, color, self, ["Rook", "Queen"])
        checkForPin(row, col, 0, -1, color, self, ["Rook", "Queen"])
        checkForPin(row, col, 0, 1, color, self, ["Rook", "Queen"])
        checkForPin(row, col, 1, 1, color, self, ["Bishop", "Queen"])
        checkForPin(row, col, -1, -1, color, self, ["Bishop", "Queen"])
        checkForPin(row, col, 1, -1, color, self, ["Bishop", "Queen"])
        checkForPin(row, col, -1, 1, color, self, ["Bishop", "Queen"])
        """
        canMove = []
        row = position[0]
        col = position[1]
        canMove = [
            checkForCheckDiagonal(row, col, 1, 0, friendlyColor, self, ["Rook", "Queen"])[0],
            checkForCheckDiagonal(row, col, -1, 0, friendlyColor, self, ["Rook", "Queen"])[0],
            checkForCheckDiagonal(row, col, 0, -1, friendlyColor, self, ["Rook", "Queen"])[0],
            checkForCheckDiagonal(row, col, 0, 1, friendlyColor, self, ["Rook", "Queen"])[0],
            checkForCheckDiagonal(row, col, 1, 1, friendlyColor, self, ["Bishop", "Queen"])[0],
            checkForCheckDiagonal(row, col, 1, -1, friendlyColor, self, ["Bishop", "Queen"])[0],
            checkForCheckDiagonal(row, col, -1, 1, friendlyColor, self, ["Bishop", "Queen"])[0],
            checkForCheckDiagonal(row, col, -1, -1, friendlyColor, self, ["Bishop", "Queen"])[0]          
        ]
        

        if len(checkForCheckAroundKing(row, col, self, friendlyColor)) == 0:
            canMove.append(False)
        else:
            canMove.append(True)

        if True in canMove:
            return True

        return False

    def Protected(self, position):
        piece = self.getPiece(position)
        enemySquares = []
        for row in self.board:
            for x in row:
                if self.isPiece(x, True) and x.color == piece.color:
                    x.checkAttackingPieces(self, False)
                    for attacked in x.defendingPieces:
                        if attacked:
                            enemySquares.append(attacked)

        if position in enemySquares:
            return True

        return False

    def promotePawn(self, position, piece):
        ogPiece = self.getPiece(position)
        newPiece = piece(position[0], position[1], ogPiece.color, ogPiece.pieceNum)
        newPiece.firstMove = False
        self.replacePiece(position, newPiece)

def simulateGame(moves):
    sim = game()
    sim.boardType = "FAKE"
    for move in moves:
        selectedPiece = move[0]
        newLocation = move[1]
        sim.movePiece(selectedPiece[0], selectedPiece[1], newLocation[0], newLocation[1])
        sim.refreshGame()
    
    return sim

def simulateCheck(moves, color):
    sim = simulateGame(moves)
    sim.refreshGame()
    return sim.getCheck(color)