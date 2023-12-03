total = 0
with open("schematic.txt", 'r') as f:
    mat = []
    for line in f:
        mat.append(line.strip())

    num_rows = len(mat)
    num_cols = len(mat[0])

    for j in range(num_rows):
        digit_builder = ""
        digit_start_index = -1
        for i in range(num_cols):
            curr_char = mat[j][i]

            if curr_char.isdigit():
                digit_builder += curr_char
                if digit_start_index == -1:
                    digit_start_index = i
                if i != num_cols-1:
                    continue
            if len(digit_builder) == 0:
                continue

            # is valid number
            is_valid = False
            for m in range(digit_start_index-1, digit_start_index+len(digit_builder)+1):
                for n in range(j-1, j+2):
                    if m < 0 or m >= num_cols:
                        continue
                    if n < 0 or n >= num_rows:
                        continue

                    surrounding_char = mat[n][m]
                    if surrounding_char != '.' and not surrounding_char.isdigit():
                        is_valid = True
                        break
            
            if is_valid:
                curr_int = int(digit_builder)
                total += curr_int

            # Reset
            digit_start_index = -1
            digit_builder = ""

print(total)