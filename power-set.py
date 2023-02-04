from copy import deepcopy

def powerset_helper(pointer, choices_made,input, result):
    if pointer < 0:
        result.append(deepcopy(choices_made))
        return

    choices_made.append(input[pointer])
    powerset_helper(pointer-1, choices_made, input, result)
    
    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, input, result)


def powerset(input):
    result = []
    powerset_helper(len(input)-1, [], input, result)
    return result



print(powerset([1,2,3])) # expects [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]


  