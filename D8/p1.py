import math

# Taken from google AI directly :)
def euclidean_distance(point1, point2):
    distance_squared = 0
    for i in range(len(point1)):
        distance_squared += (point2[i] - point1[i]) ** 2
    return math.sqrt(distance_squared)



input = open("./D8/input.txt", "r").readlines()
#print(input)

# Make input useable
input_list = []
for i in input:
    #print(i)
    int_list = i.split(',')
    temp_list = []
    for j in int_list:
        #print(j)
        temp_list.append(int(j))
    input_list.append(temp_list)
#print(input_list)

# point1 = input_list[0]
# point2 = input_list[19]
distance_list = []
for item in input_list:
    for index in range(len(input_list)-1):
        # Check every item in the list against every other item in the list
        if item == input_list[index]:
            continue
        distance = euclidean_distance(item, input_list[index])
        #print(distance)
        distance_list.append([item, input_list[index], distance])
    #print(distance_list)
    #distance_list.sort()
print(distance_list)

## Thoughts on next steps...
# Loop through distance_list and count the number of duplicates?
seen = set()
duplicate_count = 0
for item in distance_list:
    if item in seen:
        duplicate_count +=1
    else:
        seen.add(item)
print(duplicate_count)