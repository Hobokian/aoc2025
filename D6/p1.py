input = open("./D6/input.txt", "r").read()
#print(input.split('\n'))

grid = [line.strip().split(' ') for line in input.split('\n')]
#print(grid)
filtered_list = []
for item in grid:
    #print(item)
    filtered_list.append([item for item in item if item.strip()])
#print(filtered_list)

# get len of lists in filtered list
list_of_list_length = 0
for i in filtered_list:
    list_of_list_length = len(i)
    break

total_of_total = 0
for i in range(list_of_list_length):
    numbers = []
    operator = ""
    for list in filtered_list:
        if list[i].isnumeric():
            numbers.append(list[i])
        else:
            operator = list[i]
    print(numbers)
    print(operator)

    # do the math
    total = 0
    for item in numbers:
        if total == 0:
            total += int(item)
            continue
        if operator == '*':
            total *= int(item)
        if operator == '+':
            total += int(item)
        if operator == '-':
            total -= int(item)
        if operator == '/':
            total /= int(item)
    #print(total)
    total_of_total += total
print(total_of_total)



# for item in grid:
#     print(item)

# for item in input.split('\n'):
#     item = item.strip()
#     print(item)
#     exit(0)
# grid = [line for line in input.split('\n')]
# print(grid)
