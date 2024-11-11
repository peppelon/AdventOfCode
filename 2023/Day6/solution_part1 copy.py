total = 0
with open('data.txt','r') as data:
    time = data.readline().strip().split(' ')[1:]
    time = int(''.join(time).strip())
    
    record = data.readline().strip().split(' ')[1:]
    record = int(''.join(record).strip())

    for i in range(1, time):
        speed = i
        time_left = time - i
        distance = speed * time_left
        if distance > record:
            total += 1

print(total)