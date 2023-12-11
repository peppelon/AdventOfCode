expansion_value = 1_000_000
total = 0
with open("data.txt", 'r') as f:

    universe = [line.strip() for line in f.readlines()]
    rows = len(universe)
    cols = len(universe[0])

    # get galaxy locations
    galaxies = []
    for j, r in enumerate(universe):
        for i, c in enumerate(universe[0]):
            curr = universe[j][i]
            if curr == '#':
                galaxies.append((i,j))

    galaxies_original = galaxies.copy()
    
    # expand universe
    index_checked = 0
    while index_checked < rows:
        if '#' not in universe[index_checked]:
            # universe.insert(index_checked, '.'*cols)
            galaxies = [(i, j) if galaxies_original[index][1] < index_checked else (i, j+expansion_value-1)
            for index, (i, j) in enumerate(galaxies)]
        index_checked += 1

    index_checked = 0
    while index_checked < cols:
        universe_col = [row[index_checked] for row in universe]
        if '#' not in universe_col:
            galaxies = [(i, j) if galaxies_original[index][0] < index_checked else (i+expansion_value-1, j)
            for index, (i, j) in enumerate(galaxies)]
        index_checked += 1

    # calculate distances (manhattan)
    for src in galaxies:
        for dst in galaxies:
            if src == dst:
                continue
            distance = abs(src[0] - dst[0]) + abs(src[1] - dst[1])
            total += distance
print(total // 2)