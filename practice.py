
def climbStairs(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbStairs(n-1) + climbStairs(n-2)

print(climbStairs(12))

def fib(n, memo=None):
    if memo is None:
        memo = {0:1, 1:1}
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

print(fib(9))

def bottom_fib(n):
    fib_table = [0] * (n+1)
    fib_table[0] = 1
    fib_table[1] = 1
    for i in range(2, n+1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
    return fib_table[n]

print(bottom_fib(9))


def palindrome(s):
    if len(s) < 2:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])



