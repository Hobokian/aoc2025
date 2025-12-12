input = open("./D4/input.txt", "r").read()
#print(input)

grid = [[str(i) for i in line] for line in input.split('\n')]
grid_temp = [[str(i) for i in line] for line in input.split('\n')]
#print(grid)
access_counter = 0
for row in range(len(grid)): # row
    surround_ats_counter = 0
    for col in range(len(grid)): # col
        if grid[row][col] == "@":
            # Check all 8 surrounding tiles for other rolls
            if col-1 >= 0 and grid[row][col-1] == "@":
                surround_ats_counter +=1
            if col+1 < len(grid) and grid[row][col+1] == "@":
                surround_ats_counter +=1
            if row-1 >= 0 and grid[row-1][col] == "@":
                surround_ats_counter +=1
            if row+1 < len(grid) and grid[row+1][col] == "@":
                surround_ats_counter +=1
            if col-1 >= 0 and row-1 >= 0 and grid[row-1][col-1] == "@":
                surround_ats_counter +=1
            if col+1 < len(grid) and row+1 < len(grid) and grid[row+1][col+1] == "@":
                surround_ats_counter +=1
            if col-1 >= 0 and row+1 < len(grid) and grid[row+1][col-1] == "@":
                surround_ats_counter +=1
            if row-1 >= 0 and col+1 < len(grid) and grid[row-1][col+1] == "@" :
                    surround_ats_counter +=1
            if surround_ats_counter < 4:
                access_counter +=1
                surround_ats_counter = 0
                # convert the @ to an X
                grid_temp[row][col] = 'x'
            surround_ats_counter = 0
#print(grid)
for item in grid_temp:
    #print(item)
    for i in item:
        print(i, end="")
    print("")
print(access_counter)
