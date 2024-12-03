import re

with open("data.txt", "r") as data:
    content = data.read()

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, content)
    total = 0
    for x,y in matches:
        total += int(x) * int(y)

    print(total)