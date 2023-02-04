def MajorityBirthdays(days):
    return helper(days, 0, len(days)-1)

def helper(days, low, high):
    #base case when days arr size is 1
    if(low == high):
        return days[low]
    
    #find mid in the array
    mid = (high - low) //2 + low
        
    #recursively call each half
    left = helper(days, low, mid)
    right = helper(days, mid+1, high)
    
    # if left and right have same majority element return either left or right
    if left == right: return left
       
    #Find the majority in the left half and right half that match the
    #majority element found returned by previous divide steps
    left_counter = 0
    for i in range(low, high+1):
        if days[i] == left: left_counter += 1
    right_counter = 0
    for i in range(low, high + 1):
        if days[i] == right: right_counter += 1
    if left_counter > right_counter: return left
    else: return right
