import re
from math import lcm

with open("map.txt", 'r') as m:
    instructions = m.readline().strip()
    m.readline() # remove empty line

    nodes = {}
    for line in m:
        node, pair = line.strip().split('=')
        node = node.strip()
        pair = re.findall('[A-Z]+', pair)
        nodes[node] = pair


    
    current_nodes = [n for n in nodes.keys() if n[2] == 'A']
    total = [0] * len(current_nodes)
    for i, current_node in enumerate(current_nodes):
        print(current_node)
        instruction_index = 0
        while not current_node.endswith('Z'):
            current_instruction = instructions[instruction_index]

            if current_instruction == 'L':
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]

            total[i] +=1
            instruction_index += 1
            if instruction_index >= len(instructions):
                instruction_index = 0

    print(lcm(*total))