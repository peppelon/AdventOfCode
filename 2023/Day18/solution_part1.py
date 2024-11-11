testing = False

def coords_between_points(prev, curr):
    vertical_dist = abs(curr[1]-prev[1])
    horizontal_dist = abs(curr[0]-prev[0])
    path = []
    if horizontal_dist == 0:
        start_point = min(curr[1], prev[1])
        path = [(curr[0], i) for i in range(start_point, start_point + vertical_dist+1)]
    else:
        start_point = min(curr[0], prev[0])
        path = [(j, curr[1]) for j in range(start_point, start_point + horizontal_dist+1)]

    return path


dig_coords = []
dig_color = {}
with open("test.txt" if testing else "file.txt", "r") as file:
    previous_coords = (0,0)
    for line in file.readlines():
        dir, dist, color = line.split(" ")

        curr_coords = previous_coords
        if dir == 'R':
            curr_coords = (previous_coords[0] + int(dist), previous_coords[1])
        elif dir == 'L':
            curr_coords = (previous_coords[0] - int(dist), previous_coords[1])
        elif dir == 'U':
            curr_coords = (previous_coords[0], previous_coords[1] - int(dist))
        elif dir == 'D':
            curr_coords = (previous_coords[0], previous_coords[1] + int(dist))
        
        path = coords_between_points(previous_coords, curr_coords)
        for coords in path:
            dig_coords.append(coords)
            dig_color[coords] = color.replace('(', '').replace(')','')

        previous_coords = curr_coords

    min_x = min([x for x,_ in dig_coords])
    max_x = max([x for x,_ in dig_coords]) + abs(min_x)
    min_y = min([y for _,y in dig_coords])
    max_y = max([y for _,y in dig_coords]) + abs(min_y)
    

def create_dig(max_x, max_y, x_offset, y_offset, coords):
    dig = []
    for i in range(max_y+1):
        dig.append(['.'] * (max_x+1))

    for x, y in coords:
        dig[y + y_offset][x + x_offset] = '#'

    return dig

def draw_dig(dig):
    dig = [''.join(row) for row in dig]
    print('\n'.join(dig))

def fill_dig(dig, max_x, max_y):
    toggle_count = 0
    for j in range(max_y):
        inside = False
        prev = ''
        for i in range(max_x):
            curr = dig[j][i]
            if (curr != '#' and prev == "#"):
                toggle_count += 1
                inside = not inside

            if curr == '.':
                dig[j][i] = '#' if inside else '.'
            prev = curr
    print(f'Toggle count: {toggle_count}')
    return dig

def count_dig(dig):
    count = 0
    for row in dig:
        count += ''.join(row).count("#")
    return count

x_offset = abs(min_x)
y_offset = abs(min_y)

dig = create_dig(max_x, max_y, x_offset, y_offset, dig_coords)
draw_dig(dig)
dig = fill_dig(dig, max_x, max_y)




print(count_dig(dig))



