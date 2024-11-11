testing = True

flipped_plane = []
with open("test.txt" if testing else "file.txt", "r") as file:
    
    plane = []
    for row in file.readlines():
        plane.append(row.rstrip())

    flipped_plane = list(map(list, zip(*plane)))

sum = 0
row_length = len(row)
for row in flipped_plane:
    lower_bound = 0
    for idx, char in enumerate(row):
        match char:
            case 'O':
                sum += (row_length - lower_bound)
                lower_bound += 1
                continue
            case '.':
                continue
            case '#':
                lower_bound = idx+1
                continue
    
print(sum)


    