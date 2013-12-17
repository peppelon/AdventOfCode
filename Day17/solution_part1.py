import numpy as np
from collections import namedtuple

testing = True

heat_map_list = []
with open("test.txt" if testing else "file.txt", "r") as file:
    for line in file.readlines():
        heat_map_list.append(list(line.strip()))

heat_map = np.array([i for i in heat_map_list])

# define point tuple
Point = namedtuple('Point', ['coords', 'parent', 'g', 'h', 'f'])

def manhattan_distance(src, dst):
    return abs(src[0] - dst[0]) + abs(src[1] - dst[1])

def get_neighbors(x_dim, y_dim, point):
    neighbors = []
    x, y = point
    for j in [y-1, y+1]:
        if j < 0 or j >= y_dim: continue
        neighbors.append((x, j))
        
    for i in [x-1, x+1]:
        if i < 0 or i >= x_dim: continue
        neighbors.append((i,y))
    return neighbors

def print_path(heat_map_, point_list, end_point):

    next_point: Point = point_list[end_point]
    while next_point.parent != (-1,-1):
        x, y = next_point.parent
        heat_map_[y][x] = "#"
        next_point = point_list[next_point.parent]
    heat_map_ = [''.join(lst) for lst in heat_map_]
    print('\n'.join(heat_map_))



# add start point
x_dim, y_dim = heat_map.shape
start_point = Point((0,0), (-1,-1), 0, 0, 0)
end_point = (x_dim-1, y_dim-1)
optimal_value = dict()
to_traverse = [start_point]

# pick next node
goal_found = False
while to_traverse and not goal_found:
    # print(f"Lenght of to traverse: {len(to_traverse)}")
    to_traverse.sort(key=lambda x: -x.f) # best last
    curr_point = to_traverse.pop() # take last

    neighbors = get_neighbors(x_dim, y_dim, curr_point.coords)
    for neighbor in neighbors:

        g = curr_point.g + int(heat_map[neighbor])
        h = manhattan_distance(neighbor, end_point)
        f = g + h

        if neighbor == end_point: # we found the goal
            optimal_value[end_point] = Point(end_point, curr_point.coords, g, h, f)
            goal_found = True
            break 

        add_to_traverse = False
        if len(to_traverse) == 0:
            add_to_traverse = True

        # check open list
        for node in to_traverse:
            if node.coords == neighbor and node.f < f:
                break # skip this neighbor
            if neighbor in optimal_value.keys():
                if optimal_value[neighbor].f < f:
                    break
            else:
                add_to_traverse = True
        
        if add_to_traverse:
            to_traverse.append(Point(neighbor, curr_point.coords, g, h, f))
    
    optimal_value[curr_point.coords] = curr_point

#print(to_traverse)
print(optimal_value[end_point])
print_path(heat_map_list, optimal_value, end_point)
print("Goal found!")

