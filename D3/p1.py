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
        try:
            if str(second_number) < battery_bank[indextwo]:
                second_number = battery_bank[indextwo]
        except IndexError:
            continue
    print("Second number: " + second_number)
    print("Battery is: " + first_number + second_number)
    battery_number = str(first_number) + str(second_number)
    print("BN: " + str(battery_number))
    total_number += int(battery_number)
print(total_number)



# for battery_bank in input:
#     battery_bank = battery_bank.strip()
#     print(battery_bank)
#     battery_bank_list = list(battery_bank)
#     # battery_bank_list_temp = list(battery_bank)
#     # # FIND - the 2 largest digits in the string in any order
#     # NUMBER_1 = max(battery_bank_list_temp)
#     # print(NUMBER_1)
#     # battery_bank_list_temp.remove(NUMBER_1)
#     # NUMBER_2 = max(battery_bank_list_temp)
#     # print(NUMBER_2)
#     # THEN - put (NOT ADD) them together in the original order found in the string
#     # joltage_string = ""
#     digit_one = 0
#     digit_two = 0
#     for i,battery in enumerate(battery_bank_list):
#         for j,item in enumerate(battery_bank_list):
#             if j+1 < len(battery_bank_list):
#                 if int(battery_bank_list[i]) > int(battery_bank_list[j+1]):
#                     digit_one = int(battery_bank_list[i])
#     print(digit_one)