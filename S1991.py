import sys

sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())

preorder_ans, inorder_ans, postorder_ans = '', '', ''
tree = {}

for _ in range(n):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = (left, right)

def preorder(parent):
    global preorder_ans
    if parent == '.':
        return
    preorder_ans += parent
    preorder(tree[parent][0])
    preorder(tree[parent][1])
    return preorder_ans

def inorder(parent):
    global inorder_ans
    if parent == '.':
        return
    inorder(tree[parent][0])
    inorder_ans += parent
    inorder(tree[parent][1])
    return inorder_ans

def postorder(parent):
    global postorder_ans
    if parent == '.':
        return
    postorder(tree[parent][0])
    postorder(tree[parent][1])
    postorder_ans += parent
    return postorder_ans

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))