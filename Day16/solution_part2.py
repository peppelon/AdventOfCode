testing = False

LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'

def print_beam_path(x_dim, y_dim, path):
    contraption = []
    for j in range(y_dim):
        contraption.append(list(x_dim * '.'))

    for p in path:
        x,y = p
        contraption[y][x] = '#'
    contraption = ["".join(lst) for lst in contraption]
    print('\n'.join(contraption))

contraption = []
with open("test.txt" if testing else "file.txt", "r") as file:
    for line in file.readlines():
        contraption.append(line.strip())


x_dim = len(contraption[0])
y_dim = len(contraption)

def count_energized(x_dim, y_dim, start_point, contraption):
    history = []
    beams = [start_point]
    while beams:
        beam = beams.pop()
        if beam in history:
            continue
        else:
            history.append(beam)
        x,y,dir = beam
        if dir == RIGHT:
            x += 1
        elif dir == LEFT:
            x -= 1
        elif dir == UP:
            y -= 1
        elif dir == DOWN:
            y += 1
        
        if x >= x_dim or x < 0 or y >= y_dim or y < 0:
            continue

        current_space = contraption[y][x]
        if dir == RIGHT:
            if current_space == '.' or current_space == '-':
                beams.append((x,y,RIGHT))
            elif current_space == '\\':
                beams.append((x,y,DOWN))
            elif current_space == '/':
                beams.append((x,y,UP))
            else: # |
                beams.append((x,y,UP))
                beams.append((x,y,DOWN))
            continue

        if dir == LEFT:
            if current_space == '.' or current_space == '-':
                beams.append((x,y,LEFT))
            elif current_space == '\\':
                beams.append((x,y,UP))
            elif current_space == '/':
                beams.append((x,y,DOWN))
            else: # |
                beams.append((x,y,UP))
                beams.append((x,y,DOWN))
            continue

        if dir == UP:
            if current_space == '.' or current_space == '|':
                beams.append((x,y,UP))
            elif current_space == '\\':
                beams.append((x,y,LEFT))
            elif current_space == '/':
                beams.append((x,y,RIGHT))
            else: # -
                beams.append((x,y,LEFT))
                beams.append((x,y,RIGHT))
            continue
        
        if dir == DOWN:
            if current_space == '.' or current_space == '|':
                beams.append((x,y,DOWN))
            elif current_space == '\\':
                beams.append((x,y,RIGHT))
            elif current_space == '/':
                beams.append((x,y,LEFT))
            else: # -
                beams.append((x,y,LEFT))
                beams.append((x,y,RIGHT))
            continue

    unique = set([(x,y) for x,y,_ in history])
    return len(unique)-1 # subract start

energy = []
# left side
for j in range(y_dim):
    energy.append(count_energized(x_dim, y_dim, (-1, j, RIGHT), contraption))


# right side
for j in range(y_dim):
    energy.append(count_energized(x_dim, y_dim, (x_dim, j, LEFT), contraption))

# top side
for i in range(x_dim):
    energy.append(count_energized(x_dim, y_dim, (i, -1, DOWN), contraption))

# bottom side
for i in range(x_dim):
    energy.append(count_energized(x_dim, y_dim, (i, y_dim, UP), contraption))

print(max(energy))
