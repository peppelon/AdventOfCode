with open("data.txt", 'r') as data:
    num_nice = 0

    # requirement 2
    for word in data.readlines():
        nice_word = False
        for i in range(2, len(word)):
            if word[i-2] == word[i] and word[i-1] != word[i]:
                nice_word = True
                break
        if not nice_word:
            continue

        #requirement 1
        for i in range(len(word)-2):
            substr = word[i:i+2]
            if word.find(substr, i+2) != -1:
                num_nice += 1
                break

    print(num_nice)