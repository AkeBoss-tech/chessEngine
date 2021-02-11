import pygame, sys

def runGame(board, screen):
    run = True
    
    selectedPiece = []
    mode = "ready"
    while run:
        screen.drawGrid(board.board, board.highlightedPieces)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                if len(board.highlightedPieces) == 0:
                    board.clearHighlightedPieces()
                    mode = "ready"
                screen.drawGrid(board.board, board.highlightedPieces)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x < 100 and y < 100:
                    board.undoMove()
                    continue
                
                abc = board.returnBoard()
                arrayValue, onBoard, isPiece = findWhichSquare(x, y, False, board, abc)
                if onBoard:
                    if mode == "take":
                        x = board.getLegalMoves(selectedPiece)
                        for y in x:
                            if list(y) == arrayValue:
                                board.movePiece(selectedPiece[0], selectedPiece[1], arrayValue[0], arrayValue[1])
                                board.changeTurn()
                                # print(f"\n\nThreatened: {board.Threatened(arrayValue)}")
                                # print(f"Threatening: {board.getPiece(arrayValue).attackingEnemy}")
                                # print(f"\nProtected: {board.Protected(arrayValue)}")
                                # print(f"Protecting: {board.getPiece(arrayValue).defendingPieces}")

                        mode = "reset"

                    if mode == "counting":
                        delete = False
                        for s in board.highlightedPieces:
                            if arrayValue in s:
                                board.highlightedPieces.remove(s)
                                screen.drawGrid(board.board, board.highlightedPieces)
                                delete = True

                        if delete is False:
                            if isPiece:
                                board.changeHighlightedPieces(arrayValue, "blue")
                            else:
                                board.changeHighlightedPieces(arrayValue, "green")
                        else:
                            if len(board.highlightedPieces) == 0:
                                mode == "reset"

                    if isPiece and mode == "ready" and board.getPiece(arrayValue).color == board.turn:
                        selectedPiece = arrayValue
                        board.changeHighlightedPieces(arrayValue, "red")
                        mode = "take"
                        for y in board.getLegalMoves(selectedPiece):
                            if board.isPiece(y):
                                board.changeHighlightedPieces(y, "gray")
                            else:
                                board.changeHighlightedPieces(y, "circle")

                    elif not isPiece and mode == "ready":
                        board.changeHighlightedPieces(arrayValue, "green")
                        mode = "counting"

                    elif isPiece and mode == "ready" and board.getPiece(arrayValue).color != board.turn:
                        board.changeHighlightedPieces(arrayValue, "blue")
                        mode = "counting"

                elif not onBoard:
                    mode = "reset"

                if mode == "reset":
                    selectedPiece = []
                    board.clearHighlightedPieces()
                    mode = "ready"

                screen.drawGrid(board.board, board.highlightedPieces)

def findWhichSquare(mouseX, mouseY, highlight, Board, x):
    arrayValue = ["-1", "-1"]
    for i in range(8):
        if ((i + 1) * 100) <= mouseX <= ((i + 1) * 100) + 100:
            arrayValue[1] = int(i)
            break

    for t in range(8):
        if ((t + 1) * 100) <= mouseY <= ((t + 1) * 100) + 100:
            arrayValue[0] = int(t)
            break
    
    onBoard = (True, False)["-1" in arrayValue]   

    if highlight and onBoard:
        Board.changeHighlightedPieces(arrayValue, "green")

    isPiece = False
    if onBoard:
        o = x[arrayValue[0]][arrayValue[1]]
        if o != "--":
            isPiece = True
    return arrayValue, onBoard, isPiece

def checkDiagonal(row, col, rowDirection, colDirection, board):
    possiblePos = []
    piece = board.getPiece([row, col])
    friendlyColor = piece.color
    currentRow = row
    currentCol = col
    n = 1
    while True:
        location = [currentRow + n * rowDirection, currentCol + n * colDirection]
        if not board.checkIfPossibleOnBoard(location):
            return possiblePos, []
        
        if board.isPiece(location):
            if board.getPiece(location).color == friendlyColor:
                return possiblePos, location
            elif board.getPiece(location).color != friendlyColor:
                possiblePos.append(location)
                return possiblePos, []
        else:
            possiblePos.append(location)
        
        n += 1
    
    return possiblePos, []

def returnDiagonal(row, col, rowDirection, colDirection):
    possiblePos = []
    currentRow = row
    currentCol = col
    n = 1
    while True:
        location = [currentRow + n * rowDirection, currentCol + n * colDirection]
        if not checkIfPossibleOnBoard(location):
            return possiblePos

        possiblePos.append(location)
           
        n += 1
    
    return possiblePos

def checkForPin(row, col, rowDirection, colDirection, color, board, pieceType=[]):
    pin = "Nothing"
    pinnedPiece = None
    pinningPiece = None
    fullDiagonal = returnDiagonal(row, col, rowDirection, colDirection)
    for position in fullDiagonal:
        if board.isPiece(position):
            piece = board.getPiece(position)
            if piece.color == color and pin == "Nothing":
                pin = "Possible"
                pinnedPiece = position
            elif piece.color == color and pin == "Possible":
                pin = "Nothing"
                pinnedPiece = None
            elif piece.color != color and pin == "Possible":
                if piece.type in pieceType:
                    pin = True
                    board.pinnedPieces.append(pinnedPiece)
                    pinningPiece = position
                    break
                break
    
    if pin == "Posssible" or pin == "Nothing":
        pin = False
        pinnedPiece = None

    return pin, pinnedPiece, pinningPiece

def checkForCheckDiagonal(row, col, rowDirection, colDirection, color, board, pieceType=[]):
    checkingPiece = None
    fullDiagonal = returnDiagonal(row, col, rowDirection, colDirection)
    for position in fullDiagonal:
        if board.isPiece(position):
            piece = board.getPiece(position)
            if piece.color == color and piece.type != "King":
                return False, [], []
            elif piece.color != color:
                if piece.type in pieceType:
                    return True, position, fullDiagonal[0:fullDiagonal.index(position)]
                return False, [], []
    return False, [], []

def checkForCheckAroundKing(row, col, board, color):
    possibleRows = [row - 2, row - 1, row, row + 1, row + 2]
    possibleCol = [col - 2, col - 1, col, col + 1, col + 2]
    checkingPiece = []
    itemsToRemove = []
    for x in possibleRows:
        if not 0 <= x < 8:
            itemsToRemove.append(x)

    for item in itemsToRemove:
        possibleRows.remove(item)

    itemsToRemove = []
    for x in possibleCol:
        if not 0 <= x < 8:
            itemsToRemove.append(x)

    for item in itemsToRemove:
        possibleCol.remove(item)

    for r in possibleRows:
        for c in possibleCol:
            if board.isPiece([r, c]):
                piece = board.getPiece([r, c])
                if [row, col] in piece.controllingSquares and piece.color != color and piece.type != "Rook" and piece.type != "Queen" and piece.type != "Bishop":
                    checkingPiece.append([r, c])

    return checkingPiece

def checkIfPossibleOnBoard(position):
    onBoard = False
    if 0 <= position[0] < 8 and 0 <= position[1] < 8:
        onBoard = True

    return onBoard