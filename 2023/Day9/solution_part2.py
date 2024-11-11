from functools import reduce

total = 0

with open('data.txt', 'r') as f:
    for line in f:
        last_digit = []
        diff_list = [int(x) for x in line.strip().split(' ') if x.lstrip('-').isdigit()]
        
        last_digit.append(diff_list[0])
        while True:
            temp_list = []
            for x, y in zip(diff_list[0::], diff_list[1::]):
                temp_list.append(y-x)
            
            if all([x == 0 for x in temp_list]) or temp_list == []:
                break

            last_digit.append(temp_list[0])
            diff_list = temp_list
        
        last_digit.append(0)
        last_digit.reverse()
        sub_tot = reduce(lambda x,y: y-x, last_digit)
        total += sub_tot
        

print(total)