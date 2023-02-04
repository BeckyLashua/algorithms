def checkPalindrome_1(string, k):
    def helper(str, reversed_str, m, n):
        if m == 0:
            return n 
        if n == 0:
            return m

        if str[m-1] == reversed_str[n-1]:
            return helper(str, reversed_str, m-1, n-1)
        output = 1 + min(helper(str, reversed_str, m-1, n), 
                        helper(str, reversed_str, m, n-1))
        return output 

    reversed_str = string[::-1]
    return helper(string, reversed_str, len(string), len(reversed_str)) <= (k * 2)

# use a dp cache
def checkPalindrome_2(string, k):
    dp = [[0 for x in range(len(string) + 1)] for y in range(len(string) + 1)]

    reversed_str = string[::-1]

    for i in range(0, len(string) + 1):
        for j in range(0, len(string) + 1):
            if i == False:
                dp[i][j] = j
            elif j == False:
                dp[i][j] = i
            elif string[i-1] == reversed_str[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
    return dp[len(string)][len(string)] <= (k * 2)

