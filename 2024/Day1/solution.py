with open("data.txt", "r") as data:

    left = []
    right = []
    for line in data.readlines():
        l, _,_, r = line.strip().split(" ")

        left.append(int(l))
        right.append(int(r))
    

    right_dict = {x:right.count(x) for x in right}

    sums = 0
    for val in left:
        sums+=val* right_dict.get(val, 0)

    # left.sort()
    # right.sort()

    # sums = 0
    # for l, r in zip(left, right):
    #     print(f'{l}-{r} = {l-r}')
    #     sums += abs(l-r)
    print(sums)
    