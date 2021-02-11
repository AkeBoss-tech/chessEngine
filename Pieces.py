from Board import *
from Utilities import *

def checkIfInBoard(row, col):
    onBoard = False
    if 0 <= row < 8 and 0 <= col < 8:
        onBoard = True

    return onBoard

class Piece():
    def __init__(self, row, col, color, type):
        self.row = row
        self.col = col
        self.color = color
        self.type = type
        self.startingPos = (row, col)
        self.firstMove = True
        self.defendingPieces = []
        self.attackingEnemy = []
        self.controllingSquares = []

    def changePos(self, newPos):
        self.row = newPos[0]
        self.col = newPos[1]
        self.firstMove = False

class Pawn(Piece):
    def __init__(self, row, col, color, pieceNum):
        super().__init__(row, col, color, "Pawn")
        self.pieceNum = pieceNum

    def checkAttackingPieces(self, Board, only=True):
        possiblePos = []
        self.defendingPieces = []
        self.attackingEnemy = []
        self.controllingSquares = []
        if self.color == "white":
            if self.firstMove:
                attackPiece = [self.row - 1, self.col - 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row - 1, self.col + 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row - 1, self.col]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    if x == "--":
                        possiblePos.append(attackPiece)
                        attackPiece = [self.row - 2, self.col]
                        onBoard = checkIfInBoard(attackPiece[0], attackPiece[1])
                        if onBoard:
                            x = Board.board[attackPiece[0]][attackPiece[1]]
                            if x == "--":
                                possiblePos.append(attackPiece)

            else:
                attackPiece = [self.row - 1, self.col - 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row - 1, self.col + 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row - 1, self.col]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    if x == "--":
                        possiblePos.append(attackPiece)

        elif self.color == "black":
            if self.firstMove:
                attackPiece = [self.row + 1, self.col - 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row + 1, self.col + 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row + 1, self.col]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    if x == "--":
                        possiblePos.append(attackPiece)
                        attackPiece = [self.row + 2, self.col]
                        onBoard = checkIfInBoard(attackPiece[0], attackPiece[1])
                        if onBoard:
                            x = Board.getPiece(attackPiece)
                            if x == "--":
                                possiblePos.append(attackPiece)

            else:
                attackPiece = [self.row + 1, self.col - 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row + 1, self.col + 1]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    self.controllingSquares.append(attackPiece)
                    if x != "--":
                        color = x.color
                        if color == self.color:
                            self.defendingPieces.append(attackPiece)
                        else:
                            self.attackingEnemy.append(attackPiece)
                            possiblePos.append(attackPiece)

                attackPiece = [self.row + 1, self.col]
                if Board.checkIfPossibleOnBoard(attackPiece):
                    x = Board.getPiece(attackPiece)
                    if x == "--":
                        possiblePos.append(attackPiece)

        return possiblePos

class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color, "King")
        self.specialMove = []

    def checkAttackingPieces(self, board, only=True):
        possiblePos = []
        self.specialMove = []
        self.defendingPieces = []
        self.controllingSquares = []
        self.attackingEnemy = []
        possibleRows = [self.row - 1, self.row, self.row + 1]
        possibleCol = [self.col - 1, self.col, self.col + 1]
        for x in possibleRows:
            if not 0 <= x < 8:
                possibleRows.remove(x)

        for x in possibleCol:
            if not 0 <= x < 8:
                possibleCol.remove(x)

        for row in possibleRows:
            for col in possibleCol:
                isItSafe = board.canKingMove([row, col], self.color)
                if board.board[row][col] == "--" and not isItSafe:
                    possiblePos.append((row, col))
                    self.controllingSquares.append((row, col))
                elif not isItSafe:
                    if board.board[row][col].color is self.color:
                        self.defendingPieces.append((row, col))
                        self.controllingSquares.append((row, col))
                    else:
                        self.attackingEnemy.append((row, col))
                        self.controllingSquares.append((row, col))
                        if not board.Protected([row, col]):
                            possiblePos.append((row, col))


        castlingPositions = [
            [self.row, self.col + 1],
            [self.row, self.col + 2]
        ]

        rookLocation = [self.row, self.col + 3]
        
        if self.firstMove and not board.isPiece(castlingPositions[0]) and not board.isPiece(castlingPositions[1]) and board.isPiece(rookLocation):
            if board.getPiece(rookLocation).type == "Rook" and not board.canKingMove([self.row, self.col], self.color) and not board.canKingMove(castlingPositions[0], self.color) and not board.canKingMove(castlingPositions[1], self.color):
                self.specialMove.append([castlingPositions[1], rookLocation, castlingPositions[0]])
                possiblePos.append(castlingPositions[1])

        castlingPositions = [
            [self.row, self.col - 1],
            [self.row, self.col - 2],
            [self.row, self.col - 3]
        ]

        rookLocation = [self.row, self.col - 4]
        
        if self.firstMove and not board.isPiece(castlingPositions[0]) and not board.isPiece(castlingPositions[1]) and not board.isPiece(castlingPositions[2]) and board.isPiece(rookLocation):
            if board.getPiece(rookLocation).type == "Rook" and not board.canKingMove([self.row, self.col], self.color) and not board.canKingMove(castlingPositions[0], self.color) and not board.canKingMove(castlingPositions[1], self.color):
                self.specialMove.append([castlingPositions[1], rookLocation, castlingPositions[0]])
                possiblePos.append(castlingPositions[1])
        
        return possiblePos

class Queen(Piece):
    def __init__(self, row, col, color, pieceNum):
        super().__init__(row, col, color, "Queen")
        self.pieceNum = pieceNum

    def checkAttackingPieces(self, board, only=True):
        possiblePos = []
        self.controllingSquares = []
        a, a2 = checkDiagonal(self.row, self.col, 1, 0, board)
        b, b2 = checkDiagonal(self.row, self.col, -1, 0, board)
        c, c2 = checkDiagonal(self.row, self.col, 0, -1, board)
        d, d2 = checkDiagonal(self.row, self.col, 0, 1, board)
        da, da2 = checkDiagonal(self.row, self.col, 1, 1, board)
        db, db2 = checkDiagonal(self.row, self.col, -1, -1, board)
        dc, dc2 = checkDiagonal(self.row, self.col, 1, -1, board)
        dd, dd2 = checkDiagonal(self.row, self.col, -1, 1, board)
        for thing in a, b, c, d, da, db, dc, dd:
            for thing in thing:
                possiblePos.append(thing)
        
        self.defendingPieces = []
        for z in a2, b2, c2, d2, da2, db2, dc2, dd2:
            self.defendingPieces.append(z)

        for pos in possiblePos:
            self.controllingSquares.append(pos)

        for pos in self.defendingPieces:
            self.controllingSquares.append(pos)

        return possiblePos

class Rook(Piece):
    def __init__(self, row, col, color, pieceNum):
        super().__init__(row, col, color, "Rook")
        self.pieceNum = pieceNum

    def checkAttackingPieces(self, board, only=True):
        possiblePos = []
        self.controllingSquares = []  
        a, a2 = checkDiagonal(self.row, self.col, 1, 0, board)
        b, b2 = checkDiagonal(self.row, self.col, -1, 0, board)
        c, c2 = checkDiagonal(self.row, self.col, 0, -1, board)
        d, d2 = checkDiagonal(self.row, self.col, 0, 1, board)
    
        for thing in a, b, c, d:
            for thing in thing:
                possiblePos.append(thing)
        
        self.defendingPieces = []
        for z in a2, b2, c2, d2:
            self.defendingPieces.append(z)
        for pos in possiblePos:
            self.controllingSquares.append(pos)

        for pos in self.defendingPieces:
            self.controllingSquares.append(pos)

        return possiblePos

class Knight(Piece):
    def __init__(self, row, col, color, pieceNum):
        super().__init__(row, col, color, "Knight")
        self.pieceNum = pieceNum

    def checkAttackingPieces(self, board, only=True):
        possiblePos = [
            [self.row-2, self.col+1],
            [self.row-2, self.col-1],
            [self.row+2, self.col+1],
            [self.row+2, self.col-1],
            [self.row+1, self.col+2],
            [self.row+1, self.col-2],
            [self.row-1, self.col+2],
            [self.row-1, self.col-2]
        ]
        self.controllingSquares = []
        removeLocation = []

        for piece in possiblePos:
            if board.checkIfPossibleOnBoard(piece):
                if board.isPiece(piece):
                    if board.getPiece(piece).color == self.color:
                        removeLocation.append(piece)
                        self.defendingPieces.append(piece)
            else:
                removeLocation.append(piece)

        for item in removeLocation:
            possiblePos.remove(item)
        
        for pos in possiblePos:
            self.controllingSquares.append(pos)

        for pos in self.defendingPieces:
            self.controllingSquares.append(pos)

        return possiblePos

class Bishop(Piece):
    def __init__(self, row, col, color, pieceNum):
        super().__init__(row, col, color, "Bishop")
        self.pieceNum = pieceNum

    def checkAttackingPieces(self, board, only=True):
        possiblePos = []
        self.controllingSquares = []
        da, da2 = checkDiagonal(self.row, self.col, 1, 1, board)
        db, db2 = checkDiagonal(self.row, self.col, -1, -1, board)
        dc, dc2 = checkDiagonal(self.row, self.col, 1, -1, board)
        dd, dd2 = checkDiagonal(self.row, self.col, -1, 1, board)
        for thing in da, db, dc, dd:
            for thing in thing:
                possiblePos.append(thing)
        
        self.defendingPieces = []
        for z in da2, db2, dc2, dd2:
            self.defendingPieces.append(z)
        for pos in possiblePos:
            self.controllingSquares.append(pos)

        for pos in self.defendingPieces:
            self.controllingSquares.append(pos)

        return possiblePos

