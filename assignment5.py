# problem 1
class Node:
    def __init__(self, key: int, p = None, l = None, r = None, h = 1):
        self.left = l
        self.right = r
        self.parent = p
        self.value = key
        self.height = h

class Tree:
    def __init__(self, key):
        self.root = Node(key)

def left_rotate(T: Tree, x: Node):
    y = x.right
    x.right = y.left
    if y.left:
        y.left.parent = x
    y.parent = x.parent
    if not x.parent:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y
    update_height(x)
    update_height(y)

def right_rotate(T: Tree, y: Node):
    x = y.left
    y.left = x.right
    if x.right:
        x.right.parent = y
    x.parent = y.parent
    if not y.parent:
        T.root = x
    elif y == y.parent.left:
        y.parent.left = x
    else:
        y.parent.right = x
    x.right = y
    y.parent = x
    update_height(x)
    update_height(y)

def avl_insert(T: Tree, key: int):
    cur, cur_p = T.root, None
    while cur:
        cur_p = cur
        if key == cur.value:
            print("key exists:", key)
            return
        elif key < cur.value:
            cur = cur.left
        else:
            cur = cur.right
    new_node = Node(key, cur_p)
    if not cur_p:
        T.root = new_node
    elif key < cur_p.value:
        cur_p.left = new_node
    else:
        cur_p.right = new_node
    avl_fixup(T, new_node)

def update_height(node: Node):
    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0
    node.height = 1 + max(left_height, right_height)

def get_balance(node: Node) -> int:
    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0
    return left_height - right_height

def avl_fixup(T: Tree, z: Node):
## Write Your Code Here ##
## You may add more helper functions ##
    while z:
        update_height(z)
        balance = get_balance(z)

        if balance > 1 and get_balance(z.left) >= 0: # Left Left
            right_rotate(T, z)
        elif balance < -1 and get_balance(z.right) <= 0: # Right Right
            left_rotate(T, z)
        elif balance > 1 and get_balance(z.left) < 0:  # Left Right
            left_rotate(T, z.left)
            right_rotate(T, z)
        elif balance < -1 and get_balance(z.right) > 0: # Right Left
            right_rotate(T, z.right)
            left_rotate(T, z)

        z = z.parent

def find_min(node: Node) -> Node:
    while node.left is not None:
        node = node.left
    return node

def transplant(T: Tree, u: Node, v: Node):
    if u.parent is None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v is not None:
        v.parent = u.parent

def avl_delete(T: Tree, key: int):
## Write Your Code Here ##
## You may add more helper functions ##
    node = T.root
    while node is not None and key != node.value:
        if key < node.value:
            node = node.left
        else:
            node = node.right
    if node is None:
        print("Key not found:", key)
        return
    if node.left is None:
        transplant(T, node, node.right)
        balance_point = node.parent
    elif node.right is None:
        transplant(T, node, node.left)
        balance_point = node.parent
    else:
        successor = find_min(node.right)
        balance_point = successor if successor.parent != node else successor.parent
        if successor.parent != node:
            transplant(T, successor, successor.right)
            successor.right = node.right
            successor.right.parent = successor
        transplant(T, node, successor)
        successor.left = node.left
        successor.left.parent = successor

    while balance_point is not None:
        update_height(balance_point)
        avl_fixup(T, balance_point)
        balance_point = balance_point.parent

###################################
### Below are sample functions for testing.
### You may add more test cases.
###################################
from typing import List
def printBST(tree: Tree):
    print_helper(tree.root, 1)

def print_helper(root: Node, depth: int):
    tab = " "*(depth*5)
    if not root:
        print(tab, "None")
        return
    print_helper(root.right, depth + 1)
    print(tab + str(root.value) + "(" + str(root.height) + ")")
    print_helper(root.left, depth + 1)

def arrayToBST(nums: List[int]):
    tree = Tree(nums[0])
    for n in nums[1:]:
        avl_insert(tree, n)
        printBST(tree)
    return tree

tree1 = arrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("-----------------------------------------------")
avl_delete(tree1, 3)
printBST(tree1)
print("-----------------------------------------------")
avl_delete(tree1, 1)
printBST(tree1)
print("-----------------------------------------------")
avl_delete(tree1, 10)
printBST(tree1)

print("-----------------------------------------------")
print("-----------------------------------------------")

# More  tests:
tree2 = arrayToBST([10, 5, 11, 20, 30])
print("-----------------------------------------------")
avl_delete(tree2, 5)
printBST(tree2)

print("-----------------------------------------------")
print("-----------------------------------------------")

tree3 = arrayToBST([50, 20, 60, 10, 25, 55, 70, 5, 15])
print("-----------------------------------------------")
avl_delete(tree3, 55)
printBST(tree3)
print("-----------------------------------------------")
avl_delete(tree3, 70)
printBST(tree3)

print("-----------------------------------------------")
print("-----------------------------------------------")


# Problem 2
def minimumRemoval(activities):
## Write Your Code Here ##
    activities.sort(key=lambda x: x[1])
    last_finish_time = -1
    schedule_count = 0
    for start, finish in activities:
        if start >= last_finish_time:
            schedule_count += 1
            last_finish_time = finish
    return len(activities) - schedule_count

## test cases
print(minimumRemoval([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]))# this should return 7.
print(minimumRemoval([(1,2),(2,3),(3,4),(1,3)])) # this should return 1.
print(minimumRemoval([(1,2),(1,2),(1,2)])) # this should return 2.
print(minimumRemoval([(1,2),(2,3)])) # this should return 0.
print(minimumRemoval([(0,1),(0,1),(0,1)])) # this should return 2.
print(minimumRemoval([(0,1),(1,2)])) # this should return 0.