import re

with open("data.txt", "r") as data:
    content = data.read()
    dos = content.split("do()")

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    total = 0
    for do in dos:
        enabled = do.split("don't()")[0] # only the first is enabled by do
        matches = re.findall(pattern, enabled)
    
        for x,y in matches:
            total += int(x) * int(y)

    print(total)