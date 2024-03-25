def maxSubArray(A: list):
    maxi = A[0]
    current = A[0]
    start = 0
    end = 0
    s = 0
    
    for i in range(1, len(A)):
        if A[i] > current + A[i]:
            current = A[i]
            s = i
        else:
            current += A[i]
        if current > maxi:
            maxi = current
            start = s
            end = i
    return (A[start:end+1], maxi)

print(maxSubArray([-100])) # returns ([-100], -100)
print(maxSubArray([13, -100, 20])) # returns ([20], 20)
print(maxSubArray([-100, 20, -10, 60, 80])) # returns ([20, -10, 60, 80], 150)
print(maxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
# returns ([18, 20, -7, 12], 43)
print(maxSubArray([1, 2, 3, -2, 5])) # returns ([1, 2, 3, -2, 5], 9)
print(maxSubArray([-2, -3, 4, -1, -2, 1, 5, -3])) # returns ([4, -1, -2, 1, 5], 7)
print(maxSubArray([1])) # returns ([1], 1)