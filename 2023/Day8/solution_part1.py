import re
total = 0

with open("map.txt", 'r') as m:
    instructions = m.readline().strip()
    m.readline() # remove empty line

    nodes = {}
    for line in m:
        node, pair = line.strip().split('=')
        node = node.strip()
        pair = re.findall('[A-Z]+', pair)
        nodes[node] = pair

    instruction_index = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        current_instruction = instructions[instruction_index]

        if current_instruction == 'L':
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]

        total += 1
        instruction_index += 1
        if instruction_index >= len(instructions):
            instruction_index = 0


print(total)