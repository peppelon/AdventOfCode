with open("data.txt", 'r') as data:

    safe = 0
    
    for line in data.readlines():
        decreasing=False
        nums = list(map(int, line.split(" ")))
        
        # decreasing = nums[0] > nums[1]
        # is_valid = True
        # prev = nums[0]
        # first = True
        # for i, num in enumerate(nums[1:]):
        #     # print(f"prev: {prev}: curr: {num}")
        #     if decreasing:
        #         if prev-3 <= num and prev > num:
        #             pass
        #         else:
        #             is_valid=False
        #             break
        #     else:
        #         if prev+3 >= num and prev < num:
        #             pass
        #         else:
        #             is_valid=False
        #             break
        #     prev = num

        # if is_valid:
        #     safe +=1
        #     continue


        # for j in range(len(nums)):
        #     changed_nums = nums.copy()
        #     changed_nums.pop(i)
        #     print(changed_nums)
        #     decreasing = changed_nums[0] > changed_nums[1]
        #     is_valid = True
        #     prev = changed_nums[0]
        #     for i, num in enumerate(changed_nums[1:]):

        #         # print(f"prev: {prev}: curr: {num}")
        #         if decreasing:
        #             if prev-3 <= num and prev > num:
        #                 pass
        #             else:
        #                 is_valid=False
        #                 break
        #         else:
        #             if prev+3 >= num and prev < num:
        #                 pass
        #             else:
        #                 is_valid=False
        #                 break
        #         prev = num

        #     if is_valid:
        #         safe +=1
        #         break


        # if not is_valid:
        #     print(f'nums: {nums}')
        def check_valid(lst:list)->bool:
            result = []
            for curr_, next_ in zip(lst, lst[1:]):
                result.append(curr_ - next_)
            is_decreasing = map(lambda x: x > 0 and x <= 3,  result)
            is_increasing = map(lambda x: x < 0 and x >= -3,  result)
            if all(is_decreasing) or all(is_increasing):
                return True
            else:
                return False

        for j in range(len(nums)):
            changed_nums = nums.copy()
            changed_nums.pop(j)

            if check_valid(changed_nums):
                safe += 1
                break




print(safe)