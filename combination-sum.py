from copy import deepcopy

def combination_helper(num, combination, result, remainder, max_len):
    if len(combination) == max_len:
        if remainder == 0:
            result.append(deepcopy(combination))
        return
    if remainder < 0:
        return

    for i in range(num + 1, l0):
        if i <= remainder:
            combination.append(i)
            combination_helper(i, combination, result, remainder - i, max_len)
        #backtrack
        combination.pop()

def combination(n, k):
    result = []
    combination_helper(0, [], result, n, k)

print(combination(3,6))

 
'''from copy import deepcopy

def combination_sum_helper(nums, start, result, remainder, combination):

    if(remainder == 0):
        result.append(deepcopy(combination))
        return
    elif( remainder <0):
        return # sum exceeded the target
    for i in range(start, len(nums)):
        combination.append(nums[i])
        combination_sum_helper(nums, i, result, remainder-nums[i], combination)
        #backtrack
        combination.pop()


def combination_sum(nums, target):
    result = []
    combination_sum_helper(nums,0, result, target,[])
    print(result)

print(combination_sum([2,3,6,7], 7 ))'''