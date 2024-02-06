import time
import copy

PUZZLE_NUM = 1

# VALIDATION FUNCTIONS
def getCorner(row: int, col: int) -> (int,int):
    cornerCoord = lambda x : x // 3 * 3 
    return cornerCoord(row), cornerCoord(col)

def checkValid(place: int, puzzle: list[list[int]], row: int, col: int) -> bool:
    # check row
    for num in puzzle[row]:
        if num == place:
            return False
    
    # check columns
    for rowCheck in puzzle:
        if rowCheck[col] == place:
            return False
    
    # check box
    corner = getCorner(row,col) # get the top left corner for the box that coord is in 
    for i in range(corner[0], corner[0]+3):
        for j in range(corner[1],corner[1]+3):
            if puzzle[i][j] == place:
                return False
    
    return True

def checkValidForInput(puzzle: list[list[int]], row: int, col: int) -> bool:
    place = puzzle[row][col]
    # check row
    for countCol,num in enumerate(puzzle[row]):
        if num == place and countCol != col:
            return False
    
    # check columns
    for countRow,rowCheck in enumerate(puzzle):
        if rowCheck[col] == place and countRow != row:
            return False
    
    # check box
    corner = getCorner(row,col) # get the top left corner for the box that coord is in 
    for i in range(corner[0], corner[0]+3):
        for j in range(corner[1],corner[1]+3):
            if puzzle[i][j] == place and i != row and j != col:
                return False
    
    return True

def checkInputValid(puzzle: list[list[int]]) -> bool:
    for rowNum,row in enumerate(puzzle):
        for colNum,num in enumerate(row): 
            if num != 0:
                if checkValidForInput(puzzle,rowNum,colNum) == False or num > 9 or num < 0:
                    return False
    return True

# MOVEMENT FUNCTIONS
def increment(row: int,col: int) -> (int,int):
    col += 1
    if (col > 8):
        row += 1
        col = 0

    return row,col

def reduce(row: int, col: int) -> (int,int):
    col -= 1
    if (col < 0):
        row -= 1
        col = 8  

    return row,col

def goForward(row: int, col: int, zeroPuzzle: list[list[int]]) -> (int,int):
    valid: bool = False
    while not valid:
        row,col = increment(row,col)
        valid = True if (row == 9 and col == 0) or zeroPuzzle[row][col] == 0 else False
    
    return row,col

def goBack(row: int, col: int, zeroPuzzle: list[list[int]]) -> (int,int):
    valid: bool = False
    while not valid:
        row,col = reduce(row,col)
        valid = True if zeroPuzzle[row][col] == 0 else False

    return row,col

def findValidBackSpace(row,col,puzzle,zeroPuzzle):
    validBackSpace = False
    while not validBackSpace:
        validBackSpace = True
        row,col = goBack(row,col,zeroPuzzle)
        if puzzle[row][col] < 9:
            curVal = puzzle[row][col] + 1
            puzzle[row][col] = 0
        else:
            puzzle[row][col] = 0
            validBackSpace = False  
    return row,col,curVal

# MAIN SOLVING FUNCTION
def solveSudoku(puzzle: list[list[int]]) -> None:
    zeroPuzzle = copy.deepcopy(puzzle)
    curVal: int = 1
    solved: bool = False
    calNum: int = 0 # counts number of calculations
    col: int = 0 # point to num in row
    row: int = 0 # point to row

    # go to first index which is zero
    if puzzle[row][col] != 0: row,col = goForward(row,col,zeroPuzzle)

    while not(solved):
        validPlace = checkValid(curVal,puzzle,row,col)

        if validPlace: 
            puzzle[row][col] = curVal
            curVal = 1
            row,col = goForward(row,col,zeroPuzzle)
            solved = True if (row == 9 and col == 0) else False
        else:
            if (curVal >= 9):
                row,col,curVal = findValidBackSpace(row,col,puzzle,zeroPuzzle)
            else:
                curVal += 1
        
        calNum += 1
        if (calNum > 900_000): raise Exception("ERROR: Time limit exceeded")

    return puzzle,calNum

def main():
    if PUZZLE_NUM == 1:
        puzzle = [
            [0,0,9, 0,0,0, 0,1,5],
            [5,0,0, 4,0,9, 7,0,0],
            [4,7,3, 5,6,1, 9,0,0],
            [0,0,0, 7,4,0, 0,9,6],
            [0,0,0, 0,0,0, 0,8,0],
            [0,0,4, 8,3,0, 1,5,0],
            [1,3,5, 9,0,0, 0,0,2],
            [0,0,6, 2,5,7, 0,3,0],
            [7,2,0, 0,1,0, 0,0,9]
        ]
    elif PUZZLE_NUM == 2:
        puzzle = [
            [2,6,0,3,0,0,0,1,0],
            [5,8,0,4,0,0,7,0,0],
            [0,0,0,0,6,0,0,2,8],
            [0,0,0,8,3,0,0,0,7],
            [0,1,2,7,0,5,3,0,0],
            [0,5,0,0,0,0,0,0,0],
            [0,4,6,0,0,0,0,0,1],
            [7,0,0,0,0,0,0,4,0],
            [0,3,5,0,0,0,6,0,0]
        ]
    else:
        puzzle = [
            [0,7,0,0,0,6,0,0,5],
            [0,4,0,8,0,0,0,0,0],
            [8,0,5,0,0,1,0,3,0],
            [9,0,6,1,0,0,0,0,4],
            [0,0,0,0,0,3,2,0,0],
            [0,8,0,0,0,0,0,0,0],
            [5,0,1,9,0,0,0,0,6],
            [0,0,7,0,0,0,0,0,0],
            [0,0,0,0,6,0,0,4,0]
        ]

    startTime: time = time.time()
    puzzle,calNum = solveSudoku(puzzle)
    endTime: time = time.time()

    for row in puzzle: print(row)
    print(f"\nFINAL TIME: {endTime - startTime}")
    print(f"NUM OF CALCULATIONS: {calNum:,}")


if __name__ == "__main__":
    main()