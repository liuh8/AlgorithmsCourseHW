# Problem 1
import heapq

def sort(A):
    heap = []
    result = []
    
    for i, lst in enumerate(A):
        heapq.heappush(heap, (lst[0], i, 0))
    
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        if elem_idx + 1 < len(A[list_idx]):
            next_val = A[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result

# Test cases
print("-------- Problem 1 ------------------")
print(sort([[1]]) == [1]) # returns [1]
print(sort([[2], [1]]) == [1, 2]) # returns [1, 2]
print(sort([[2, 3, 3, 4], [1, 5], [1, 2, 4]]) == [1, 1, 2, 2, 3, 3, 4, 4, 5]) # returns [1, 1, 2, 2, 3, 3, 4, 4, 5]
print(sort([[10, 100], [1, 1, 1], [1, 1000]]) == [1, 1, 1, 1, 10, 100, 1000]) # returns [1, 1, 1, 1, 10, 100, 1000]

# Problem 2
def k_largest(A, k):
    heap = []
    for i, lst in enumerate(A):
        heapq.heappush(heap, (-lst[-1], i, len(lst) - 1))
    
    while k > 0:
        val, list_idx, elem_idx = heapq.heappop(heap)
        k -= 1
        if k == 0:
            return -val
        if elem_idx > 0:
            next_val = A[list_idx][elem_idx - 1]
            heapq.heappush(heap, (-next_val, list_idx, elem_idx - 1))

print("-------- Problem 2 ------------------")
print(k_largest([[1]], 1) == 1)
print(k_largest([[2], [1]], 2) == 1)
print(k_largest([[2, 3, 3, 4], [1, 5], [1, 2, 4]], 4) == 3)
print(k_largest([[10, 100], [1, 1, 1], [1, 1000]], 7) == 1)

# Problem 3
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def k_largest_bst(root, k):
    def reverse_inorder(node):
        if node is None or count[0] >= k:
            return
        reverse_inorder(node.right)
        count[0] += 1
        if count[0] == k:
            result[0] = node.value
            return
        reverse_inorder(node.left)
    count = [0]
    result = [None]
    reverse_inorder(root)
    return result[0]

# test
print("-------- Problem 3 ------------------")
root = Node(41)
root.left = Node(20)
root.right = Node(65)
root.left.left = Node(11)
root.left.right = Node(29)
root.left.right.right = Node(32)
root.right.left = Node(50)
root.right.right = Node(91)
root.right.right.left = Node(72)
root.right.right.right = Node(99)

k = 4
print(k_largest_bst(root, k) == 65)
