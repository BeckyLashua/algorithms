def getTesla(M):
    m = len(M)
    n = len(M[0])

    dp = [[0 for x in range(n)] for y in range(m)]

    for x in range(m-1, -1, -1):
        for y in range(n-1, -1, -1):
            if x == m - 1 and y == n - 1:
                dp[x][y] = max(1-M[x][y], 1)
            elif x == m-1:
                right_cell = dp[x][y+1]
                dp[x][y] = max(right_cell - M[x][y], 1)
            elif y == n-1:
                down_cell = dp[x+1][y]
                dp[x][y] = max(down_cell - M[x][y], 1)
            else:
                right_cell = dp[x][y+1]
                down_cell = dp[x+1][y]
                dp[x][y] = min(max(right_cell - M[x][y], 1), max(down_cell-M[x][y], 1))

    return dp[0][0]



