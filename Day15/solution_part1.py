testing = False

sum = 0
with open("test.txt" if testing else "file.txt", "r") as file:
    for word in file.readline().strip().split(','):
        chars = list(word)
        hash = 0
        for c in chars:
            hash += ord(c)
            hash *= 17
            hash %= 256
        sum += hash

print(sum)