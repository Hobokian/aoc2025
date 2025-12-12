input = open("./D5/input.txt", "r").read()
#print(input)

fresh_id_ranges = []
avail_ingredient_ids = []

#print(input.splitlines())

for item in input.splitlines():
    if "-" in item:
        fresh_id_ranges.append(item)
    else:
        avail_ingredient_ids.append(item)

# Remove blank link from avail_ingredient_ids
avail_ingredient_ids = [x for x in avail_ingredient_ids if x.strip()]

#print(fresh_id_ranges)
#print(avail_ingredient_ids)

fresh_ingredients = 0
for i in avail_ingredient_ids:
    #print(i)
    for j in fresh_id_ranges:
        #print(j)
        # Split the range into 2 number and make that the bounds of the next if
        min = j.split('-')[0]
        max = j.split('-')[1]
        if int(i) >= int(min) and int(i) <= int(max):
            fresh_ingredients +=1
            break
print(fresh_ingredients)