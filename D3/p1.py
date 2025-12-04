input = open("./D3/input.txt", "r").readlines()
#print(input)

for battery_bank in input:
    battery_bank = battery_bank.strip()
    print(battery_bank)
    battery_bank_list = list(battery_bank)
    # battery_bank_list_temp = list(battery_bank)
    # # FIND - the 2 largest digits in the string in any order
    # NUMBER_1 = max(battery_bank_list_temp)
    # print(NUMBER_1)
    # battery_bank_list_temp.remove(NUMBER_1)
    # NUMBER_2 = max(battery_bank_list_temp)
    # print(NUMBER_2)
    # THEN - put (NOT ADD) them together in the original order found in the string
    # joltage_string = ""
    digit_one = 0
    digit_two = 0
    for i,battery in enumerate(battery_bank_list):
        for j,item in enumerate(battery_bank_list):
            if j+1 < len(battery_bank_list):
                if int(battery_bank_list[i]) > int(battery_bank_list[j+1]):
                    digit_one = int(battery_bank_list[i])
    print(digit_one)