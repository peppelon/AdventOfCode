with open("data.txt", 'r') as data:

    antenna_coords = {}
    height = 0
    for y, lines in enumerate(data.readlines()):
        width = len(lines)
        for x, char in enumerate(lines.strip()):
            if char == '.':
                continue
            
            if char in antenna_coords:
                antenna_coords[char].append((x,y))
            else:
                antenna_coords[char] = [(x,y)]
        height += 1
    
    def within_map(height, width, x, y):
        return x >= 0 and x < width and y >= 0 and y < height

    resonance_coords = set()
    for antenna_set in antenna_coords.values():
        for i, antenna1 in enumerate(antenna_set):
            for j, antenna2 in enumerate(antenna_set[i:]):
                if antenna1 == antenna2:
                    continue
                x_dist, y_dist = antenna1[0] - antenna2[0], antenna1[1] - antenna2[1]
                
                resonance1 = (antenna1[0] + x_dist, antenna1[1] + y_dist)
                resonance2 = (antenna2[0] - x_dist, antenna2[1] - y_dist)

                if within_map(height, width, resonance1[0], resonance1[1]):
                    resonance_coords.add(resonance1)
                if within_map(height, width, resonance2[0], resonance2[1]):
                    resonance_coords.add(resonance2)

with open("data.txt", 'r') as data:
    area = [list(line.strip()) for line in data.readlines()]
    for coord in resonance_coords:
        area[coord[1]][coord[0]] = '#'
    print('\n'.join([''.join(a) for a in area]))
    print(len(resonance_coords))