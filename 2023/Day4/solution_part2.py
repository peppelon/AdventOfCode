total = 0
with open("cards.txt") as f:
    line_number = 1
    instances_of_cards = {}
    for line in f:
        if str(line_number) not in instances_of_cards.keys():
            instances_of_cards[str(line_number)] = 1
        else:
            instances_of_cards[str(line_number)] += 1

        left, right = line.strip().split('|')
        scratched_numbers_str = left.split(':')[1]
        scratched_numbers = set([int(i) for i in scratched_numbers_str.strip().split(' ') if i.isdigit()])
        correct_numbers = set([int(i) for i in right.strip().split(' ') if i.isdigit()])
        winning_numbers = scratched_numbers.intersection(correct_numbers)

        if winning_numbers:
            for line_index in range(line_number+1, line_number + len(winning_numbers) + 1):
                if str(line_index) in instances_of_cards.keys():
                    instances_of_cards[str(line_index)] += instances_of_cards[str(line_number)]
                else:
                    instances_of_cards[str(line_index)] = instances_of_cards[str(line_number)]

        line_number +=1
    print(instances_of_cards)
    for amount in instances_of_cards.values():
        total += amount

print(total)
