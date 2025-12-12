input = open("./D7/input.txt", "r").read()
#print(input.split('\n'))
split_counter = 0
grid = [[str(i) for i in line] for line in input.split('\n')]
#print(grid)
for row in range(len(grid)-1): # row
    for col in range(len(grid)-1): # col
        if grid[row][col] == "S":
            # set the south tile to a |
            grid[row+1][col] = '|'
        elif grid[row][col] == "|":
            if grid[row+1][col] == '^':
                split_counter +=1
                grid[row+1][col-1] = '|'
                grid[row+1][col+1] = '|'
            else:
                grid[row+1][col] = '|'
#print(grid)
for item in grid:
    #print(item)
    for i in item:
        print(i, end="")
    print("")
print(split_counter)