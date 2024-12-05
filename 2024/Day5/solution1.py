with open("data.txt", "r") as data:
    rules = {}
    while True:
        rule = data.readline()
        if rule == "\n":
            break
        first, second = rule.strip().split("|")

        if second in rules:
            rules[second].add(first)
        else:
            rules[second] = set()
            rules[second].add(first)
    
    total = 0
    for update in data.readlines():
        update_list = update.strip().split(",")
        update_list.reverse()
        correct_order = True
        for i, num in enumerate(update_list):
            come_before = rules.get(num)
            if come_before == None:
                if  i != (len(update_list)-1): # last (first) update
                    correct_order = False
                    break

            nums_before = set(update_list[(i+1):])
            if nums_before and nums_before.intersection(come_before) != nums_before:
                correct_order = False
                break

        if correct_order:   
            total += int(update_list[len(update_list)//2])
                
    print(total)

