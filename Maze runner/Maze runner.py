#the task was to find the exit from the maze which is located in the maze.txt file as a matrix
#1 is the wall, 0 is the trail

def found(pathArr, finPoint):
    weight = 1
    for i in range(len(pathArr) * len(pathArr[0])):
        for y in range(len(pathArr)):
            for x in range(len(pathArr[y])):
                if pathArr[y][x] == weight:
                    # Вниз
                    if y > 0 and pathArr[y - 1][x] == 0:
                        pathArr[y - 1][x] = weight + 1
                        # Вверх
                    if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
                        pathArr[y + 1][x] = weight + 1
                    # Вправо
                    if x > 0 and pathArr[y][x - 1] == 0:
                        pathArr[y][x - 1] = weight + 1
                    # Влево
                    if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
                        pathArr[y][x + 1] = weight + 1
                    # Конечная точка
                    if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
                        pathArr[finPoint[0]][finPoint[1]] = weight + 1
                        return True
        weight += 1
    return False

def printPath(pathArr, finPoint):
    y = finPoint[0]
    x = finPoint[1]
    weight = pathArr[y][x]
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y > 0 and pathArr[y - 1][x] == weight:
            result[weight] = 'Up'
            y -= 1
        elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
            result[weight] = 'Down'
            y += 1
        elif x > 0 and pathArr[y][x - 1] == weight:
            result[weight] = 'Right'
            x -= 1
        elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
            result[weight] = 'Left'
            x += 1
    return result[1:]


maze = []
with open("maze.txt") as myFile:
    for line in myFile:
        maze.append(line.replace('\n', '').split(' '))

ii = 0
for i in maze:
    jj = 0
    for j in i:
        if j == 'A':
            maze[ii][jj] = 1
            pozIn = (ii, jj)
        elif j == 'B':
            maze[ii][jj] = 0
            pozOut = (ii, jj)
        elif j == '1':
            maze[ii][jj] = -1
        else:
            maze[ii][jj] = 0
        jj += 1
    ii += 1

if not found(maze, pozOut):
    print("No route found")
else:
    result = printPath(maze, pozOut)

    for i in maze:
        for line in i:
            print("{:^3}".format(line), end=" ")
        print()
    print(result)
