with open("data.txt", 'r') as data:
    num_nice = 0
    vowels = "aeiou"
    forbidden = ["ab", "cd", "pq", "xy"]

    for word in data.readlines():
        # Requirement 3
        not_nice = False
        for string in forbidden:
            if string in word:
                not_nice = True
        if not_nice:
            continue

        num_vowels = 0
        has_double_letters = False
        prev_char = ""
        for char in word:
            if char == prev_char:
                has_double_letters = True
            if char in vowels:
                num_vowels += 1
            prev_char = char
        
        if num_vowels >= 3 and has_double_letters:
            num_nice +=1

    print(num_nice)