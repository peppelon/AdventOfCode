with open("data.txt", "r") as data:
    
    map_ = [list(line.strip()) for line in data.readlines()]
    width = len(map_[0])
    height = len(map_)
    max_steps = width * height

    # find guard coords
    for i, line in enumerate(map_):        
        if '^' in line:
            loc = line.index("^")
            guard_pos = (loc, i)
    def guard_path(the_map, pos, max_steps):
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)] # up, right, down, left, ...
        visited_pos = set()
        visited_pos.add(guard_pos)
        curr_dir = 0
        num_steps = 0
        while num_steps < max_steps:
            next_pos = (pos[0] + dirs[curr_dir][0], pos[1] + dirs[curr_dir][1])
            if next_pos[0] < 0 or next_pos[0] >= width or next_pos[1] < 0 or next_pos[1] >= height:
                return visited_pos
            
            
            match map_[next_pos[1]][next_pos[0]]:
                case '#':
                    curr_dir = (curr_dir + 1) % 4 # rotate 90 deg
                case '.' | '^':
                    pos = next_pos
                    visited_pos.add((pos))
                case _:
                    break

            num_steps += 1
        return []
        
    visited_steps = guard_path(map_, guard_pos, max_steps)

    total_loops = 0
    for x, y in visited_steps:
        old_val = map_[y][x]
        map_[y][x] = "#" # replace with block
        if guard_path(map_, guard_pos, max_steps) == []:
            total_loops += 1
        map_[y][x] = old_val
    # print('\n'.join([''.join(i) for i in map_]))
    print(total_loops)