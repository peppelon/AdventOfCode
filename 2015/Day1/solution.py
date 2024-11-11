with open("data.txt", "r") as data:
    
    floor = 0
    reached_basement = False
    for i, c in enumerate(data.read()):
        floor += 1 if c == '(' else -1
        if floor == -1 and not reached_basement:
            print(f'He reaches the bBasement at: {i+1}')
            reached_basement = True

    print(f'He ends at floor: {floor}')
    