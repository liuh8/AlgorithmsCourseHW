# Name: Hongyu Liu
# Assignment 3

# Question 1
def quickSort(A):
    if len(A) < 2:
        return A
    i, j = threePartition(A)
    return quickSort(A[:i]) + A[i:j+1] + quickSort(A[j+1:])

def threePartition(A):
    n = len(A)
    pivot = A[n - 1] 
    i, j = 0, 0
    lt, eq, gt = 0, 0, n - 1

    while eq <= gt:
        if A[eq] < pivot:
            A[lt], A[eq] = A[eq], A[lt]
            lt += 1
            eq += 1
        elif A[eq] == pivot:
            eq += 1
        else:
            A[eq], A[gt] = A[gt], A[eq]
            gt -= 1
    i = lt
    j = gt - 1
    return i, j

print("---- Question 1 ----------------")
print(quickSort([1, 2, 4, 1, 2, 4, 3])) # [1, 1, 2, 2, 3, 4, 4]
print(quickSort([4, 5, 3, 7, 2, 1, 6])) # [1, 2, 3, 4, 5, 6, 7]
print(quickSort([10, 7, 8, 9, 1, 5]))   # [1, 5, 7, 8, 9, 10]
print(quickSort([1, 3, 3, 3, 2]))       # [1, 2, 3, 3, 3]
print(quickSort([3, 3, 3]))             # [3, 3, 3]

# Question 2
def median(X, Y):
    if len(X) > len(Y):
        X, Y = Y, X
    x, y = len(X), len(Y)
    low, high = 0, x

    while low <= high:
        i = (low + high) // 2
        j = (x + y + 1) // 2 - i
        
        max_Left = float('-inf') if i == 0 else X[i - 1]
        min_Left = float('inf') if i == x else X[i]
        max_Right = float('-inf') if j == 0 else Y[j - 1]
        min_Right = float('inf') if j == y else Y[j]

        if max_Left <= min_Right and max_Right <= min_Left:
            if (x + y) % 2 == 0:
                return (max(max_Left, max_Right) + min(min_Left, min_Right)) / 2
            else:
                return max(max_Left, max_Right)
        elif max_Left > min_Right:
            high = i - 1
        else:
            low = i + 1

print("---- Question 2 ----------------")
print(median([1], [2])) # return 1.5
print(median([1, 2], [3, 4])) # returns 2.5
print(median([2, 3], [1, 4])) # returns 2.5
print(median([1,3,5,7], [2,4,6,8])) # returns 4.5
print(median([1,2,3,4], [5,6,7,8])) # returns 4.5
print(median([1,3,5,7,9], [2,4,6,8,10])) # returns 5.5
print(median([1,3,7,8,9], [2,4,5,6,10])) # returns 5.5
print(median([10,20,30,100], [15,40,60,90])) # returns 35.0

# Question 3
def median2(X, Y):
    if len(X) > len(Y):
        X, Y = Y, X
    x, y = len(X), len(Y)
    low, high, mid = 0, x, (x + y + 1) // 2

    while low <= high:
        i = (low + high) // 2
        j = mid - i
        
        if i < x and Y[j-1] > X[i]:
            low = i + 1
        elif i > 0 and X[i-1] > Y[j]:
            high = i - 1
        else:
            if i == 0:
                max_Left = Y[j-1]
            else:
                max_Left = max(X[i-1], Y[j-1]) if i > 0 else Y[j-1]
            if (x + y) % 2 == 1:
                return max_Left
            if i == x:
                min_Right = Y[j] if j < y else float('inf')
            else:
                min_Right = min(X[i], Y[j]) if j < y else X[i]
            return (max_Left + min_Right) / 2.0
        
print("---- Question 3 ----------------")
print(median2([1], [2, 3])) # return 2.0
print(median2([1, 3], [2])) # return 2.0
print(median2([1, 2], [3, 4])) # returns 2.5
print(median2([1,2,3,4], [3,4])) # returns 3.0
print(median2([0,0,0,2,2], [1,1,1,1,1])) # returns 4.5?????? should be 1
print(median2([1,3,5,7,9], [2,4,6,8,10,11])) # returns 6.0
print(median2([1,3,7,8,9], [2,4,5,6,10,11])) # returns 6.0
print(median2([1], [2,3,4,5,6,7])) # returns 4.0
print(median2([10,20,30,100], [40,60])) # returns 35.0
print(median2([1, 3, 8], [7, 9, 10, 11])) # 8
