intervals = [[0,3], [2,5], [5,8], [8,10]]

def num__overlap_intervals(intervals):
    Sort intervals according to their start values  using mergesort

    if len(intervals) <= 1:
        return 0

    count = 0
    left = intervals[0]
    right= intervals[1]

    for interval in range(len(intervals) - 1):
        if the right interval is less than end of intervals array:
            if left.end <= right.start:
                change left pointer to right
                increment right pointer to next interval
            if left.end <= right.end:
                incremenent right pointer to next interval
                count += 1
            if left.end > right.end:
                change left pointer to right 
                increment right pointer to next interval
                count += 1
    return count
        

