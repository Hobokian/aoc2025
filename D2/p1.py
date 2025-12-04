

input = open("./D2/input.txt", "r").read().split(',')
#print(input)

for id_range in input:
    #print(id_range)
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    for i in range(start, end+1):
        #print(i)
        # Find duplicate digits
        ### DUMB WAY
        # Read each digit in $i and create new numbers for each grouping
        # For example 123123 do this:
        # 1 2 3 1 2 3
        # 12 3123
        # 123 123 - FOUND PATTERN EXIT
        for d in str(i):
            print(d)
            
        exit(0)