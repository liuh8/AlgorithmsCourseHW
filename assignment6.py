# problem 1
def longestPalindromeSubsequence(s):
    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
    
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    index = dp[0][n-1]
    lps = [""] * index
    i, j = 0, n-1
    while i <= j:
        if s[i] == s[j]:
            lps[index-1] = s[i]
            lps[len(lps)-index] = s[i]
            i += 1
            j -= 1
            index -= 1
        elif dp[i+1][j] > dp[i][j-1]:
            i += 1
        else:
            j -= 1

    return "".join(lps)

# Test
print(longestPalindromeSubsequence("banana"))  # Expected: "anana"
print(longestPalindromeSubsequence("character"))  # Expected: "carac" ?

# problem 2
def printNeatly(text, max_width):
    words = text.split()
    n = len(words)
    cost = [[0 if i == j else float('inf') for j in range(n)] for i in range(n)]
    for i in range(n):
        length = -1 
        for j in range(i, n):
            length += len(words[j]) + 1
            if length <= max_width:
                if j == n - 1:
                    cost[i][j] = 0 
                else:
                    cost[i][j] = (max_width - length) ** 3
    min_cost = [float('inf')] * n
    result = [-1] * n
    
    for i in range(n):
        for j in range(i, n):
            if cost[i][j] != float('inf'):
                if i == 0:
                    curr_cost = cost[i][j]
                else:
                    curr_cost = min_cost[i - 1] + cost[i][j]
                if curr_cost < min_cost[j]:
                    min_cost[j] = curr_cost
                    result[j] = i

    i = n
    lines = []
    while i > 0:
        next_i = result[i - 1]
        line = ' '.join(words[next_i:i])
        lines.append(line)
        i = next_i
    for line in reversed(lines):
        print(line)

# test
printNeatly("Dynamic programming is not that difficult.", 15)
print("---")
printNeatly("Algorithm is my favorite subject.", 16)
