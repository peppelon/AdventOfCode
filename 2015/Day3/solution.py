with open("data.txt", "r") as data:

    x = 0
    y = 0
    sx = 0
    sy = 0
    rx = 0
    ry = 0
    houses_santa_only = set()
    houses = set()
    santas_turn = True
    houses.add((x,y))
    houses_santa_only.add((x,y))
    for c in data.readline():
        i = 0
        j = 0
        match c:
            case '^':
                j = 1
            case '>':
                i = 1
            case '<':
                i = -1
            case _:
                j = -1

        x += i
        y += j
        houses_santa_only.add((x,y))

        if santas_turn:
            sx += i
            sy += j
            houses.add((sx,sy))
        else:
            rx += i
            ry += j
            houses.add((rx,ry))
        
        santas_turn = not santas_turn

    print(f'Solution 1: {len(houses_santa_only)}')
    print(f'Solution 2: {len(houses)}')