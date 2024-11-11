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

with open('test.txt', 'r') as f:
    pipes = [l.strip() for l in f.readlines()]

    s_row = 0
    s_col = 0
    for i, line in enumerate(pipes):
        index = line.find('S')
        if index != -1:
            s_row = i
            s_col = index
    
    size = len(pipes) # pipe map is square
    for direction, _ in moves.items():
        new_x = s_col + moves[direction][0]
        new_y = s_row + moves[direction][1]

        loop_length = 1
        incoming_direction = opposites[direction]
        loop_found = False
        while not loop_found:
            if new_y < 0 or new_y >= size or new_x < 0 or new_x >= size:
                break

            char = pipes[new_y][new_x]
            if char == 'S':
                loop_found = True
                break

            char = incoming_direction + char
            if char not in redirections.keys():
                break # no loop found

            incoming_direction = opposites[redirections[char]]
            diff_x, diff_y = moves[opposites[incoming_direction]]
            new_x += diff_x
            new_y += diff_y
            loop_length += 1

        if loop_found:
            furthest_point = loop_length // 2
            print(furthest_point)
            break


