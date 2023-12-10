# moves = {'S' : [], 
#          'n|' : ['7', 'F', '|'],
#          's|' : [ 'L', 'J', '|'],
#          'e-' : ['J', '7', '-'],
#          'w-' : ['F', 'L', '-'],
#          'nL' : ['|', 'F', '7'],
#          'eL' : ['-', '7', 'J'],
#          'nJ' : ['|', 'F', '7'],
#          'wJ' : ['-', 'F', 'L'],
#          's7' : ['|', 'L', 'J'],
#          'w7' : ['-', 'L', 'F'],
#          'sF' : ['|', 'F', '7'],
#          'eF' : ['-', 'F', 'L'],
#          ''}
redirections = {'n|' : 's', 's|' : 'n',
                'w-' : 'e', 'e-' : 'w',
                'nL' : 'e', 'eL' : 'n',
                'nJ' : 'w', 'wJ' : 'n',
                's7' : 'w', 'w7' : 's',
                'sF' : 'e', 'eF' : 's'}
opposites = {'n' : 's', 's' : 'n', 'w' : 'e', 'e' : 'w'}
moves = {'n' : (0, -1), 's' : (0, 1), 'w' : (-1, 0), 'e' : (1, 0)}

with open('data.txt', 'r') as f:
    pipes = [l.strip() for l in f.readlines()]

    s_row = 0
    s_col = 0
    for i, line in enumerate(pipes):
        index = line.find('S')
        if index != -1:
            s_row = i
            s_col = index
    
    total_in = 0
    loop_indexes = []
    size = len(pipes) # pipe map is square
    for direction, _ in moves.items():
        new_x = s_col + moves[direction][0]
        new_y = s_row + moves[direction][1]

        loop_indexes = []
        incoming_direction = opposites[direction]
        loop_found = False
        while not loop_found:
            if new_y < 0 or new_y >= size or new_x < 0 or new_x >= size:
                break

            loop_indexes.append((new_x, new_y))
            char = pipes[new_y][new_x]
            if char == 'S':
                loop_found = True
                break

            char = incoming_direction + char
            # print(f'{char} at location x={new_x} and y={new_y}')
            if char not in redirections.keys():
                break # no loop found

            incoming_direction = opposites[redirections[char]]
            diff_x, diff_y = moves[opposites[incoming_direction]]
            new_x += diff_x
            new_y += diff_y

        if loop_found:
            break

    loop_characters = [pipes[y][x] for x,y in loop_indexes]
    # replace S by correct pipe
    loop_characters = list(map(lambda x: x.replace('S', '|'),loop_characters))
    loop_characters = dict(s for s in zip(loop_indexes,loop_characters))

    inside_counter = 0
    corner = ""
    for j, row in enumerate(pipes):
        inside = False
        for i, col in enumerate(row):
            if (i,j) not in loop_indexes and inside:
                inside_counter += 1
            if (i,j) in loop_indexes:
                tile = loop_characters[(i,j)]
                if tile in "LF":
                    corner = tile
                elif tile == "J":
                    if corner == "L":
                        pass
                    elif corner == "F":
                        inside = not inside
                    corner = ""
                elif tile == "7":
                    if corner == "L":
                        inside = not inside
                    elif corner == "F":
                        pass
                    corner = ""
                elif (tile == "-") and (corner != ""):
                    pass
                elif tile == "|":
                    inside = not inside

    print(inside_counter)
