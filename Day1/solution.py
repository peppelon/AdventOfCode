numbers_as_words = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
                    "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9,
                    "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5,
                    "6" : 6, "7" : 7, "8" : 8, "9" : 9}
total_sum = 0

def find_all(string, sub_string):
    start = 0
    while True:
        start = string.find(sub_string, start)
        if start == -1:
            return
        yield start
        start += len(sub_string)

with open("words.txt", 'r') as words:
    for word in words:
        # Find numbers as strings in line
        left_most_number = 0
        left_most_index = 999999
        right_most_number = 0
        right_most_index = -1
        for num_str, value in numbers_as_words.items():
            res = list(find_all(word, num_str))
            if res: # num found
                if min(res) <= left_most_index:
                    left_most_index = min(res)
                    left_most_number = value
                if max(res) >= right_most_index:
                    right_most_index = max(res)
                    right_most_number = value

        full_number = str(left_most_number) + str(right_most_number)
        total_sum += int(full_number)

print(total_sum)