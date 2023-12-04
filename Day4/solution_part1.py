total = 0
with open("cards.txt") as f:
    for line in f:
        left, right = line.strip().split('|')
        scratched_numbers_str = left.split(':')[1]
        scratched_numbers = set([i for i in scratched_numbers_str.strip().split(' ') if i.isdigit()])
        correct_numbers = set([i for i in right.strip().split(' ') if i.isdigit()])
        winning_numbers = scratched_numbers.intersection(correct_numbers)

        if winning_numbers:
            total += 2**(len(winning_numbers)-1)

print(total)