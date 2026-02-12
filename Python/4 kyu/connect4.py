# https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python

def who_is_winner(pieces_position_list):
    player = ['Yellow','Red']
    column_heigth = [-1,-1,-1,-1,-1,-1,-1]
    grid = [[0]*7 for i in range(6)]
    column_dict = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}
    win = False
    for placement in pieces_position_list:
        if placement[2] == 'Y':
            p = 1
        else:
            p = 2
        grid[column_heigth[column_dict[placement[0]]]][column_dict[placement[0]]] = p
        column_heigth[column_dict[placement[0]]] -= 1
        win = searchForWin(grid,column_heigth,column_dict[placement[0]],column_heigth[column_dict[placement[0]]],p)
        if win == True:
            return player[p-1] 
    return "Draw"

def searchForWin(grid,column_height,x,y,p):
    if column_height[x] >= 4 and y >= 3:
        return checkUp(grid,x,y,p)
    
    if x <= 3:
        return checkRight(grid,x,y,p)
    
    if x <= 3 and y >= 4 and column_height[x+4] >= y-4:
        return checkUpRight(grid,x,y,p)
    
    if x >= 3 and y >= 4 and column_height[x-4] >= y-4:
        return checkUpLeft(grid,x,y,p)
    

def printGrid(grid):
    for line in grid:
        print(line)

# Check up only if column_height[x] >= 4 and y >= 3
def checkUp(grid,x,y,p):
    for i in range(4):
        if grid[-y-1-i][x] != p:
            return False
    return True

# Check right only if x <= 3
def checkRight(grid,x,y,p):
    for i in range(4):
        if grid[-y-1][x+i] != p:
            return False
    return True

# Check up right only if x <= 3, y >= 4, column_height[x+4] >= y - 4
def checkUpRight(grid,x,y,p):
    for i in range(4):
        if grid[-y-1-i][x+i] != p:
            return False
    return True

# Check up right only if x >= 3 3, y >= 4, column_height[x-4] >= y - 4
def checkUpLeft(grid,x,y,p):
    for i in range(4):
        if grid[-y-1-i][x-i] != p:
            return False
    return True

print(who_is_winner([ 
"C_Yellow", "E_Red", "G_Yellow", "B_Red", "D_Yellow", "B_Red", "B_Yellow", "G_Red", "C_Yellow", "C_Red",
"D_Yellow", "F_Red", "E_Yellow", "A_Red", "A_Yellow", "G_Red", "A_Yellow", "F_Red", "F_Yellow", "D_Red", 
"B_Yellow", "E_Red", "D_Yellow", "A_Red", "G_Yellow", "D_Red", "D_Yellow", "C_Red"]))


#printGrid(grid)
#print(checkUp(grid,1,0,2))
#print(checkUpRight(grid,3,0,1))