total = 0
with open("schematic.txt", 'r') as f:
    mat = []
    for line in f:
        mat.append(line.strip())

    num_rows = len(mat)
    num_cols = len(mat[0])

    for j in range(num_rows):
        for i in range(num_cols):
            curr_char = mat[j][i]

            if curr_char != '*':
                continue

            # is valid number
            surrounding_numbers = []
            spaces_checked = []
            for m in range(i-1, i+2):
                for n in range(j-1, j+2):
                    if m < 0 or m >= num_cols:
                        continue
                    if n < 0 or n >= num_rows:
                        continue
                    if (n,m) in spaces_checked:
                        continue

                    surrounding_char = mat[n][m]
                    if not surrounding_char.isdigit():
                        spaces_checked.append((n,m))
                        continue

                    full_number = surrounding_char
                    # check found number left
                    k = m-1
                    while k >= 0:
                        left_char = mat[n][k]
                        spaces_checked.append((n,k))
                        if left_char.isdigit():
                            full_number = left_char + full_number
                        else:
                            break
                        k -= 1

                    # check found number right
                    k = m+1
                    while k < num_cols:
                        right_char = mat[n][k]
                        spaces_checked.append((n,k))
                        if right_char.isdigit():
                            full_number += right_char
                        else:
                            break
                        k += 1

                    if full_number == "":
                        continue

                    surrounding_numbers.append(full_number)

            if len(surrounding_numbers) == 2:
                total += int(surrounding_numbers[0]) * int(surrounding_numbers[1])

print(total)