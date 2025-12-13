import numpy as np

input = np.loadtxt('./D8/input.txt', delimiter=',')
#print(input)

prev_point = np.array([])

circuit_list = []

for item in (input):
    print(item)

    distance = None
    index = None
    for j in range(len(input)-1):
        #print(j)
        if distance == None:
            distance = np.linalg.norm(item - input[j+1])
            index = j+1
        else:
            if distance > np.linalg.norm(item - input[j+1]):
                distance = np.linalg.norm(item - input[j+1])
                index = j+1
    print(distance)
    print(index)
#     circuit_list.append([item, input[index]])
# print(circuit_list)






#     if prev_point.size == 0:
#         prev_point = item
#     else:
#         curr_point = item
#         if prev_distance == None:
#             prev_distance = np.linalg.norm(prev_point - curr_point)
#         else:
#             if np.linalg.norm(prev_point - curr_point) < prev_distance:
#                 prev_distance = np.linalg.norm(prev_point - curr_point)

# print(prev_point)
# print(prev_distance)




# point1 = np.array([162,817,812])
# point2 = np.array([346,949,466])

# distance = np.linalg.norm(point1 - point2)
# print(f"Euclidean distance: {distance}")
# # Output: Euclidean distance: 5.196152422706632
