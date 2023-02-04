def max_independent_set(nums):
    output = []
    if len(nums) == 0: # no sum
        return output
    if len(nums) == 1: # the 1 val is sum
        output.append(nums[0])
        return output 
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    n = len(nums)
    for i in range(2, n):
        val_1 = (nums[i] + dp[i-2])
        val_2 = dp[i-1]
        dp[i] = max(val_1, val_2)
    
    max_sum = dp[-1]
    for j in range(len(nums)-1,-1,-1):
        if nums[j] > 0:
            new_sum = max_sum - nums[j]
            if new_sum == 0:
                output.append(nums[j])
                return output
            if new_sum in dp:
                output.append(nums[j])
                max_sum = new_sum
    return output



print(max_independent_set([7,2,5,8,6]))
print(max_independent_set([7,2,5,8,0,6])) #output [7,5,6] sum 18
print(max_independent_set([]))
print(max_independent_set([5]))
print(max_independent_set([5,3]))
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(max_independent_set([7, 5, -50, 50, 3, 12, 4]))

