total = 0
with open("test.txt", 'r') as f:

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

    # expand universe
    index_checked = 0
    while index_checked < rows:
        if '#' not in universe[index_checked]:
            universe.insert(index_checked, '.'*cols)
            index_checked += 1 # we have to take two steps
            rows += 1
        index_checked += 1

    galaxy_cols = [c for c, _ in galaxies]
    index_checked = 0
    while index_checked < cols:
        if not index_checked in galaxy_cols:
            for j, _ in enumerate(universe):
                universe[j] = universe[j][:index_checked] + '.' + universe[j][index_checked:]
            index_checked += 1 # we have to take two steps
            cols += 1
            galaxy_cols = [i+1 for i in galaxy_cols]
        index_checked += 1


    print(f'cols: {cols} vs. actual cols: {len(universe[0])}')
    print(f'rows: {rows} vs. actual rows: {len(universe)}')
    print([len(r) for r in universe])
    # get galaxy locations again
    galaxies = []
    for j, r in enumerate(universe):
        for i, c in enumerate(universe[0]):
            curr = universe[j][i]
            if curr == '#':
                galaxies.append((i,j))

    # calculate distances (manhattan)
    for src in galaxies:
        for dst in galaxies:
            if src == dst:
                continue

            distance = abs(src[0] - dst[0]) + abs(src[1] - dst[1])
            total += distance
print(total // 2)