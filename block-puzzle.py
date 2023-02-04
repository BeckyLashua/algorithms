
def blockpuzzle_dp(N):
    cache = [-1] * (N+1)

    def blockpuzzle_helper(cache, n):
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        if cache[n] != -1:
            return cache[n]
        cache[n] = cache[n-2] + cache[n-1]
        return cache[n]

    return blockpuzzle_helper(cache, N)


print(blockpuzzle_dp(2))