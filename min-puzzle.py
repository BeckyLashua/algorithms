import heapq

def minPuzzle(puzzle):
    # set m and n to the lengths of the 2 dimensions
    m = len(puzzle)
    n = len(puzzle[0])
    output = 0
    visited = set()   

    # Create min heap
    pq = []
    heapq.heappush(pq, (0,0,0))

    # directions to access neighbors
    x_dir = [-1, 1, 0, 0]
    y_dir = [0, 0, 1, -1]
    
    while len(pq) > 0:
        current_effort, this_x, this_y  = heapq.heappop(pq)
        output = max(current_effort, output)

        # Check to see if we have reached right bottom corner
        if (this_x == (m-1)) and (this_y == (n-1)):
            return output # return result

        visited.add((this_x, this_y))

        for i in range(4):
            temp_x = this_x + x_dir[i]
            temp_y = this_y + y_dir[i]
            if temp_x >= 0 and temp_y >= 0 and temp_x < m and temp_y < n:
                if (temp_x, temp_y) not in visited:
                    temp_effort = abs(puzzle[temp_x][temp_y] - puzzle[this_x][this_y])
                    heapq.heappush(pq, (temp_effort, temp_x, temp_y))
    return -1 













