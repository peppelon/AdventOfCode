testing = False
num_cycles = 1_000_000_000

# read file
plane = []
with open("test.txt" if testing else "file.txt", "r") as file:
    for row in file.readlines():
        plane.append(row.rstrip())

def rotate_plane_counter_clockwise(pplane):
    return ["".join(x) for x in list(zip(*pplane))[::-1]]

def rotate_plane_clockwise(pplane):
    for i in range(3):
        pplane = rotate_plane_counter_clockwise(pplane)
    return pplane

def lean_plane_left(pplane):
    new_plane = []
    row_length = len(pplane[0])
    for row in pplane:
        lower_bound = 0
        new_row = row_length * ['.']
        for idx, char in enumerate(row):
            match char:
                case 'O':
                    new_row[lower_bound] = 'O'
                    lower_bound += 1
                    continue
                case '.':
                    continue
                case '#':
                    new_row[idx] = "#"
                    lower_bound = idx+1
                    continue
        new_plane.append("".join(new_row))

    return new_plane

def print_plane(pplane):
    print('\n'.join(pplane))

def cycle(pplane):

    # north
    pplane = rotate_plane_counter_clockwise(pplane)
    pplane = lean_plane_left(pplane)

    # west-south-east
    for i in range(3):
        pplane = rotate_plane_clockwise(pplane)
        pplane = lean_plane_left(pplane)

    # rotate back north
    for i in range(2):
        pplane = rotate_plane_clockwise(pplane)

    return pplane

def plane_north_weight(pplane):

    # rotate north
    pplane = rotate_plane_counter_clockwise(pplane)

    sum = 0
    row_length = len(pplane[0])
    for row in pplane:
        for idx, char in enumerate(row):
            if char == 'O':
                sum += row_length-idx
    return sum

prev_plane = plane
history = []
while True:
    new_plane = cycle(prev_plane)
    prev_plane = new_plane

    if new_plane in history:
        break
    else:
        history.append(new_plane)

cycle_length = len(history)-history.index(prev_plane)
cycle_planes = history[-cycle_length:]

cycle_index = (num_cycles-len(history)-1) % cycle_length

print(f'{cycle_length}')

print(plane_north_weight(cycle_planes[cycle_index]))
