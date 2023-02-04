def staircase(costs):
    cache = [-1] * (len(costs))
    def helper(costs, index):
        if cache[index] != -1:
            return cache[index] 
        if index < len(costs) - 2:
            cache[index] = costs[index] + min(helper(costs, index+1), helper(costs, index+2))
        else:
            cache[index] = costs[index]
        return cache[index]
         
    return costs[0] if len(costs) == 1 else min(helper(costs, 0), helper(costs, 1))




print(staircase([10, 15, 20]))
print(staircase([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(staircase([1, 1000000000, 10, 100, 1000, 1000000000, 10000, 200000, 1000000000, 1000000]))
print(staircase([1, 1000000, 10]))



def staircase_brute(costs):
    def helper(costs, index):
        if index < len(costs) - 2:
            return costs[index] + min(helper(costs, index+1), helper(costs, index+2))
        return costs[index]
         
    return costs[0] if len(costs) == 1 else min(helper(costs, 0), helper(costs, 1))



#print(staircase_brute([10, 15, 20]))
