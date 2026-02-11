# https://www.codewars.com/kata/5868a68ba44cfc763e00008d/train/python

def interpreter(code, iterations, width, height):
    # Init the data grid
    data_grid = [[0 for i in range(width)] for j in range(height)]
    # Position in the grid
    x,y,i,j = 0,0,0,0
    output = ''


    # Execute the code
    # Make sure the program don´t exceed the code instructions 
    while j < iterations and i < len(code):
        instruction = code[i]
        match instruction:
            case 'n':
                # Move up
                    y -= 1
                    y %= height
            case 's':
                # Move down
                    y += 1
                    y %= height
            case 'e':
                # Move right
                    x += 1
                    x %= width
            case 'w':
                # Move left
                    x -= 1
                    x %= width
            case '*':
                # Flip current bit 
                data_grid[y][x] ^= not data_grid[y][x]
            case '[':
                # Jump past matching ] if bit under current pointer is 0
                if data_grid[y][x] == 0:
                    loop = 1
                    while loop > 0:
                        i += 1
                        if code[i] == '[':
                            loop += 1
                        elif code[i] == ']':
                            loop -= 1
            case ']':
                # Jump back to the matching [ if bit under current pointer is nonzero
                if data_grid[y][x] != 0:
                    loop = 1
                    while loop > 0:
                        i -= 1
                        if code[i] == '[':
                            loop -= 1
                        elif code[i] == ']':
                            loop += 1
            case _:
                j -= 1    
        i += 1
        j += 1
    # Turn the data grid into a string
    for y in range(height):
        for x in range(width):
            output += str(data_grid[y][x])
        output += '\r\n'
    return output[:-2]

if __name__ == '__main__':
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9))
    print('\n')
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9))
    print('\n')
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9))
    print('\n')
    print(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9))
    print('\n')