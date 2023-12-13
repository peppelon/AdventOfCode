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
        

        refresher_pattern = pattern.copy()
        # without smudge
        horizontal_mirror = -1
        vertical_mirror = -1
        symmetry_found = False
        while not symmetry_found:

            # horizontal symmetry
            index = 0
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
                    horizontal_mirror = index
                    break
                index += 1

            if symmetry_found:
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
                    vertical_mirror = index
                    break
                index += 1

            if symmetry_found:
                continue


        # with smudge
        row_index = 0
        col_index = -1
        symmetry_found = False
        while not symmetry_found:
            
            pattern = refresher_pattern.copy()
            # handle pattern edit
            col_index += 1
            if col_index == len(pattern[0]):
                row_index += 1
                col_index = 0
            if row_index == len(pattern):
                break
            
            # print(f'Before:')
            # [print(p) for p in pattern]
            old_row = pattern[row_index]
            smudge = '.' if old_row[col_index] == '#' else "#"
            new_row = old_row[:col_index] + smudge + old_row[(col_index+1):]
            pattern[row_index] = new_row

            # print(f'After edit:')
            # [print(p) for p in pattern]

            # horizontal symmetry
            index = 0
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
                    if index == horizontal_mirror:
                        index += 1    
                        continue
                    symmetry_found = True
                    break
                index += 1

            if symmetry_found:
                print(f'Smudge location: {col_index}, {row_index}')
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
                    if index == vertical_mirror:
                        index += 1
                        continue
                    symmetry_found = True
                    break
                index += 1

            if symmetry_found:
                print(f'Smudge location: {col_index}, {row_index}')
                result += index+1
                continue
            # print(f'{col_index}, {row_index}')      


print(result) 