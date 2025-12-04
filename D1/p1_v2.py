import re
DIAL = 50
HIT_ZERO_COUNT = 0

input = open("./D1/input.txt", "r").readlines()
#print(input)
#print(DIAL)
for rotation in input:
    rotation = rotation.strip()
    print(rotation)
    DIAL += int(re.split(r'L|R', rotation)[1])
    if DIAL > 100:
        HIT_ZERO_COUNT += DIAL // 100
        DIAL = DIAL % 100
        DIAL = 100 - DIAL
    else:
        idk
    if DIAL == 100 or DIAL == 0:
        HIT_ZERO_COUNT +=1
        DIAL = 0
    print(DIAL)
print(HIT_ZERO_COUNT)