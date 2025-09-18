BOARD_SIZE = 5

def displayChess(chBoard):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            print(chBoard[row][col], end=" ")
        print()

def isQueenPlaceValid(chBoard, crntRow, crntCol):
    # checking if queen is in the left or not
    for i in range(crntCol):
        if chBoard[crntRow][i]:
            return False
    for i, j in zip(range(crntRow, -1, -1), range(crntCol, -1, -1)):
        #checking if queen is in the left upper diagonal or not
        if chBoard[i][j]:
            return False
    for i, j in zip(range(crntRow, BOARD_SIZE), range(crntCol, -1, -1)):
        #checking if queen is in the left lower diagonal or not
        if chBoard[i][j]:
            return False
    return True

def solveProblem(chBoard, crntCol):
    #when N queens are placed successfully
    if crntCol >= BOARD_SIZE:
        return True
    # checking placement of queen is possible or not
    for i in range(BOARD_SIZE):
        if isQueenPlaceValid(chBoard, i, crntCol):
            #if validate, place the queen at place (i, col)
            chBoard[i][crntCol] = 1
            #Go for the other columns recursively
            if solveProblem(chBoard, crntCol + 1):
                return True
            #When no place is vacant remove that queen
            chBoard[i][crntCol] = 0
    return False

def displaySolution():
    chBoard = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    #starting from 0th column
    if not solveProblem(chBoard, 0):
        print("Solution does not exist")
        return False
    displayChess(chBoard)
    return True

if __name__ == "__main__":
    displaySolution()
