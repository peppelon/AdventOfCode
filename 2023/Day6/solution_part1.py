total = 1
with open('data.txt','r') as data:
    times = data.readline().strip().split(' ')[1:]
    times = [int(x) for x in times if x.isdigit()]
    
    distances = data.readline().strip().split(' ')[1:]
    distances = [int(x) for x in distances if x.isdigit()]
    
    all_solutions = []
    for t, dist_to_beat in zip(times, distances):
        num_solutions = 0
        for i in range(1, t):
            speed = i
            time_left = t - i
            distance = speed * time_left
            if distance > dist_to_beat:
                num_solutions += 1
        all_solutions.append(num_solutions)

    for s in all_solutions:
        total *= s

print(total)