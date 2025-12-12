input = open("./D3/input.txt", "r").readlines()
#print(input)

total_number = 0

for battery_bank in input:
    battery_bank = battery_bank.strip()
    print(battery_bank)
    # LOOP 1 - find largest number ignoring the last digit (I need 2 numbers so it cannot be the last one)
    first_number = -1
    first_number_index = -1
    for index in range(len(battery_bank)-1):
        #print(battery_bank[index])
        if str(first_number) < battery_bank[index]:
            first_number = battery_bank[index]
            first_number_index = index
    print("First number: " + str(first_number))
    #print("First number index: " + str(first_number_index))
    # LOOP 2 - from largest number index +1 find the next largest number
    second_number = -1
    for indextwo in range(first_number_index+1, len(battery_bank)):
        #print(battery_bank[indextwo])
        if str(second_number) < battery_bank[indextwo]:
            second_number = battery_bank[indextwo]
    print("Second number: " + second_number)
    print("Battery is: " + first_number + second_number)
    battery_number = str(first_number) + str(second_number)
    print("BN: " + str(battery_number))
    total_number += int(battery_number)
print(total_number)
