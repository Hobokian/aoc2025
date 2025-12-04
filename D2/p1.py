import re

input = open("./D2/input.txt", "r").read().split(',')
#print(input)

for id_range in input:
    LIST_OF_LISTS = []
    #print(id_range)
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    for i in range(start, end+1):
        NUMBER_LIST = []
        # Find duplicate digits
        ### NOT DUMB WAY
        # print(str(i))
        # thing = re.findall(r"(.)\1", str(i))
        # print(thing)
        #print(i)
        ###
        ### DUMB WAY
        # Read each digit in $i and create new numbers for each grouping
        # For example 123123 do this:
        # 1 2 3 1 2 3
        # 12 3123
        # 123 123 - FOUND PATTERN EXIT
        i = str(i)
        for index, item in enumerate(i):
            #print(i)
            NUMBER_LIST.append(i[index])
        print(NUMBER_LIST)
    exit(0)

# LIST_OF_LISTS = []
# LOOP - FOR EACH NUMBER ['11']
    # NUMBER_LIST = []
    # LOOP - FOR AS MANY DIGITS IN THE NUMBER - 2
        # TAKE INDEX NUMBER OF DIGITS FROM NUMBER AND SAVE IT TO A LIST - itt 1 == ['1'], itt 2 == ['11']

