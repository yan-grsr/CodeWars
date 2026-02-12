# https://www.codewars.com/kata/57658bfa28ed87ecfa00058a/train/python

def path_finder(maze):
    maze = maze.splitlines()
    n = len(maze)
    for i in range(n):
        maze[i] = list(maze[i])
    path = 0
    updated = 1
    if maze[0][0] == '.':
        maze[0][0] = 0
    else:
        return False
    
    while updated >= 1:
        updated = 0
        for y in range(n):
            for x in range(n):
                if maze[y][x] == path:
                    updated += update(maze,x,y,path,n)                
        path += 1
        if isinstance(maze[n-1][n-1],int):
            return maze[n-1][n-1]
    return False


def update(maze,x,y,path,n):
    updated = 0
    if x + 1 < n:
        if maze[y][x+1] == '.':
            maze[y][x+1] = path + 1
            updated = 1
    if x - 1 >= 0:
        if maze[y][x-1] == '.':
            maze[y][x-1] = path + 1
            updated = 1
    if y + 1 < n:
        if maze[y+1][x] == '.':
            maze[y+1][x] = path + 1
            updated = 1
    if y - 1 >= 0:
        if maze[y-1][x] == '.':
            maze[y-1][x] = path + 1
            updated = 1
    return updated    

if __name__ == '__main__':

    a = "\n".join([
    ".W.",
    ".W.",
    "..."
    ])

    print(path_finder(a))