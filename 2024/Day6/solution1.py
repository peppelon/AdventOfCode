with open("data.txt", "r") as data:
    
    map_ = [list(line.strip()) for line in data.readlines()]
    width = len(map_[0])
    height = len(map_)

    # find guard coords
    for i, line in enumerate(map_):        
        if '^' in line:
            loc = line.index("^")
            guard_pos = (loc, i)
    
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)] # up, right, down, left, ...
    visited_pos = set()
    visited_pos.add(guard_pos)
    curr_dir = 0
    while True:
        next_pos = (guard_pos[0] + dirs[curr_dir][0], guard_pos[1] + dirs[curr_dir][1])
        if next_pos[0] < 0 or next_pos[0] >= width or next_pos[1] < 0 or next_pos[1] >= height:
            break # guard exits

        match map_[next_pos[1]][next_pos[0]]:
            case '#':
                curr_dir = (curr_dir + 1) % 4 # rotate 90 deg
            case '.' | '^':
                guard_pos = next_pos
                visited_pos.add((guard_pos))
            case _:
                break


    
    # print('\n'.join([''.join(i) for i in map_]))
    print(len(visited_pos))
