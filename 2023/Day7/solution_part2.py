total = 0
lettered_label_value = {'A' : 14, 'K' : 13, 'Q' : 12, 'T' : 10, 'J' : 1}

with open("file.txt", 'r') as f:
    hand_ordering = []
    i = 1
    # primary ordering
    for line in f:
        hand_labels = {}
        hand, bid = line.strip().split(' ')
        secondary_value = []
        for label in hand:
            if label in hand_labels:
                hand_labels[label] += 1
            else:
                hand_labels[label] = 1

            if label in lettered_label_value:
                secondary_value.append(lettered_label_value[label])
            else:
                secondary_value.append(int(label))

        # if we have jokers in the hand
        if 'J' in hand_labels and hand_labels['J'] != 5:
            num_jokers = hand_labels['J']
            del hand_labels['J']
            max_label = max(hand_labels, key=hand_labels.get)
            hand_labels[max_label] += num_jokers
            
        most_labels = max(hand_labels.values())
        second_most_labels = 0
        if most_labels != 5:
            lst = list(hand_labels.values())
            lst.sort(reverse=True)
            second_most_labels = lst[1]

        hand_type_value = 0
        match((most_labels, second_most_labels)):
            case (5,0): # five of a kind
                hand_type_value = 10 
            case (4,1): # four of a kind
                hand_type_value = 9
            case (3,2): # full house
                hand_type_value = 8
            case (3,1): # three of a kind
                hand_type_value = 7
            case (2,2): # two pairs
                hand_type_value = 6
            case (2,1): # one pair
                hand_type_value = 5
            case _:
                hand_type_value = 1
            
        hand_ordering.append((hand, hand_type_value, secondary_value, bid))
    hand_ordering.sort(key=lambda x: (x[1], x[2][0], x[2][1], x[2][2], x[2][3], x[2][4]))

    for i, value in enumerate(hand_ordering):
        bid = value[3]
        total += (i+1) * int(bid)
    
print(total)