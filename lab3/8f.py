def contains_007(nums):
    for i in range(len(nums) - 2): 
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

input_list = input("input your elements:").split()
input_list = [int(x) for x in input_list]

result = contains_007(input_list)

print(result)