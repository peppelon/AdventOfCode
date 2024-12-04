with open("data.txt", 'r') as data:

    nums_xmas=0
    grid=[]
    content=[line.strip() for line in data.readlines()]
    
    height=len(content)
    width=len(content[0])
    for j in range(height):
        for i in range(width):
            if content[j][i] != "A":
                continue

            x_1 = ["M", "S"]
            x_2 = ["M", "S"]
            invalid_shape = False
            for n in range(-1, 2, 2): # only want corners
                for m in range(-1, 2, 2):
                    x = i + m
                    y = j + n
                    if x >= 0 and x < width and y >= 0 and y < height:
                        char = content[y][x]
                        if n == m and char in x_1: # diagonal 1
                            x_1.remove(char)
                        elif n != m and char in x_2:
                            x_2.remove(char)
                        else:
                            invalid_shape = True
                            break
                    else:
                        invalid_shape = True
                        break
            if not invalid_shape:
                nums_xmas += 1
    print(nums_xmas)