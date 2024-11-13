import hashlib

with open("data.txt", 'rt') as data:
    i = 0
    start_string = "00000"
    key = data.readline().strip('\n')
    while(True):
        test_key = key + str(i)
        hash_value = hashlib.md5(test_key.encode())

        if hash_value.hexdigest().startswith(start_string):
            print(i)
            break
        i += 1