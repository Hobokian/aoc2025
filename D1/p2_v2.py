DIAL = 50
HIT_ZERO_COUNT = 0

input = open("./D1/input.txt", "r").readlines()
#print(input)
#print(DIAL)
#DIAL_WAS_ZERO = False
DIAL_ROTATIONS = 0
for rotation in input:
    rotation = rotation.strip()
    print(rotation)
    
    # Left means subtract and right means add (cannot go beyond bounds 0-99)
    if "L" in rotation:
        DIAL -= int(rotation.split("L")[1])
        if DIAL < 0:
            if DIAL < -100:
                DIAL_ROTATIONS = DIAL // 100
            DIAL_ROTATIONS = abs(DIAL_ROTATIONS)
            DIAL = DIAL % 100
        if DIAL_ROTATIONS != 0:
            HIT_ZERO_COUNT += DIAL_ROTATIONS
            DIAL_ROTATIONS = 0
        elif DIAL == 100 or DIAL == 0:
            HIT_ZERO_COUNT +=1
            DIAL = 0
            #DIAL_WAS_ZERO = True
        else:
            #DIAL_WAS_ZERO = False
            DIAL_ROTATIONS = 0
        print(DIAL)
    if "R" in rotation:
        DIAL += int(rotation.split("R")[1])
        if DIAL > 100:
            DIAL_ROTATIONS = DIAL // 100
            DIAL = DIAL % 100
        if DIAL_ROTATIONS != 0:
            HIT_ZERO_COUNT += DIAL_ROTATIONS
            DIAL_ROTATIONS = 0
        elif DIAL == 100 or DIAL == 0:
            HIT_ZERO_COUNT +=1
            DIAL = 0
            #DIAL_WAS_ZERO = True
        else:
            #DIAL_WAS_ZERO = False
            DIAL_ROTATIONS = 0
        print(DIAL)
print(HIT_ZERO_COUNT)