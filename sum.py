from copy import deepcopy

def combination(n, k):
    result = []

    def combination_helper(current_i, combination, result, remaining):
        if len(combination) == k:
            if remaining == 0: 
                result.append(deepcopy(combination))
                return
        if remaining < 0:
            return
        
        for i in range(current_i + 1, 10):
            if i <= remaining:
                combination_copy = deepcopy(combination)
                combination_copy.append(i)
                combination_helper(i, combination_copy, result, remaining - i)
              
    combination_helper(0, [], result, n)
    return result




