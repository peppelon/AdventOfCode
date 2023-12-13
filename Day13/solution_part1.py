result = 0
with open("file.txt", 'r') as f:

    pattern_counter = 0
    while True:
        pattern = []

        # check end of file
        line = f.readline()
        if line == "":
            break

        # find next pattern
        line_stripped = line.rstrip()
        while line_stripped != "":
            pattern.append(line_stripped)
            line_stripped = f.readline().rstrip()
            
        # horizontal symmetry
        index = 0
        symmetry_found = False
        while not symmetry_found:
            next_index = index + 1
            if next_index == len(pattern):
                break

            if pattern[index] != pattern[next_index]:
                index += 1
                continue

            up_index = index - 1
            down_index = next_index + 1
            no_symmetry = False
            while up_index >= 0 and down_index < len(pattern):
                if pattern[up_index] != pattern[down_index]:
                    no_symmetry = True
                    break
                up_index -= 1
                down_index += 1

            if not no_symmetry:
                symmetry_found = True
                break
            index += 1

        if symmetry_found:
            result += (index+1) * 100
            continue

        # vertical symmetry
        # transpose list
        transposed_pattern = [[] for i in range(len(pattern[0]))]
        for line in pattern:
            for i,c in enumerate(line):
                transposed_pattern[i].append(c)
        pattern = transposed_pattern
        index = 0
        symmetry_found = False
        while not symmetry_found:
            next_index = index + 1
            if next_index == len(pattern):
                break

            if pattern[index] != pattern[next_index]:
                index += 1
                continue

            up_index = index - 1
            down_index = next_index + 1
            no_symmetry = False
            while up_index >= 0 and down_index < len(pattern):
                if pattern[up_index] != pattern[down_index]:
                    no_symmetry = True
                    break
                up_index -= 1
                down_index += 1

            if not no_symmetry:
                symmetry_found = True
                break
            index += 1

        if symmetry_found:
            result += index+1
            continue

        pattern_counter += 1


print(result) 