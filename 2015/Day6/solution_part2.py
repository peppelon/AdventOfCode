def toggle(val: int) -> int:
    return val + 2
def on(val: int) -> int:
    return val + 1
def off(val: int) -> int:
    return val - 1 if val > 0 else 0

with open("data.txt", 'r') as data:
    
    matrix = [[0] * 1000 for i in range(1000)]
    for line in data.readlines():
        cmds = line.split(" ")
        if cmds[0] == "toggle":
            operation, xy1, _, xy2 = cmds
        else:
            _, operation, xy1, _, xy2 = cmds

        x1, y1 = xy1.split(",")
        x2, y2 = xy2.split(",")

        op = None
        match(operation):
            case "toggle":
                op = toggle
            case "on":
                op = on
            case "off":
                op = off
            case _:
                pass
            
        for i in range(int(x1), int(x2)+1):
            for j in range(int(y1), int(y2)+1):
                matrix[j][i] = op(matrix[j][i])

    print(sum([sum(line) for line in matrix]))

           
        
