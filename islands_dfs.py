# Time complexity: O(mn) because each point in the graph is processed plus checking the four 
# spaces around it, so that is a total of 5mn, but since 5 is a constant, we can just say O(mn)
def count_islands(grid):
    m = len(grid)
    n = len(grid[0])

    def dfs(x, y):
        if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != "1":
            return 
        grid[x][y] = "x"
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y)

    islands_count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs(i, j)
                islands_count += 1
    return islands_count

example_2 = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]

grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]

example_3 = [
["0", "1"],
["0", "1"],
["0", "0"]
]


print(count_islands(grid)) #should print 1
#print(count_islands(example_2)) #should print 3
#print(count_islands(example_3))
