import re

input = open("./D2/input.txt", "r").read().split(',')
#print(input)

invalid_ids = []

for id_range in input:
    print(id_range)
    start = int(id_range.split('-')[0])
    end = int(id_range.split('-')[1])
    for number in range(start, end+1):
        #print(number)
        # Cut number in half
        number_string = str(number)
        midpoint = len(number_string) // 2
        first_half = number_string[:midpoint]
        second_half = number_string[midpoint:]
        #print(midpoint)
        #print(first_half)
        #print(second_half)
        if first_half == second_half:
            invalid_ids.append(number_string)
print(invalid_ids)
# Add invalid_ids together
inv_id_sum = 0
for id in invalid_ids:
    inv_id_sum += int(id)
print(inv_id_sum)