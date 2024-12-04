with open("data.txt", 'r') as data:

    nums_xmas=0
    grid=[]
    content=[line.strip() for line in data.readlines()]
    
    height=len(content)
    width=len(content[0])
    for j in range(height):
        for i in range(width):
            if content[j][i] != "X":
                continue
            for n in range(-1, 2):
                for m in range(-1, 2):
                    if m == 0 and n == 0:
                        continue
                    
                    coords = [(i + m * k, j + n * k) for k in range(4)]
                    coords_applicable = list(map(lambda x: x[0] >= 0 and x[0] < width and x[1] >= 0 and x[1] < height, coords))
                    if all(coords_applicable):
                        word = ''.join([content[y][x] for x,y in coords])
                        if word == "XMAS":
                            grid.extend(coords)
                            nums_xmas += 1
    print(nums_xmas)