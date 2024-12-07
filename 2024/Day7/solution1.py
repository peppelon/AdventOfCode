from operator import mul, add

with open("data.txt", 'r') as data:
    values = [list(map(int, i.replace(':','').split(" "))) for i in data]
    
    def concat(a, b):
        return int(f'{a}{b}')

    def solve(nums, ops):
        if len(nums) == 2:
            return nums[0] == nums[1]
        total, a, b, *rest = nums
        for op in ops:
            if solve([total, op(a,b)] + rest, ops):
                return total
        return 0

    solution_1 = sum([solve(value, [mul, add]) for value in values])
    print(solution_1)

    solution_2 = sum([solve(value, [mul, add, concat]) for value in values])
    print(solution_2)