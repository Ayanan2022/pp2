def has_adjacent_threes(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

input_list = input("input ").split()
input_list = [int(x) for x in input_list]

result = has_adjacent_threes(input_list)

print(result)
