def PreOrder(root):
    if root != '.':
        print(root, end = "")
        PreOrder(tree[root][0])
        PreOrder(tree[root][1])
        

def InOrder(root):
    if root != '.':
        InOrder(tree[root][0])
        print(root, end = "")
        InOrder(tree[root][1])

def PostOrder(root):
    if root != '.':
        PostOrder(tree[root][0])
        PostOrder(tree[root][1])
        print(root, end = "")

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

PreOrder('A')
print()
InOrder('A')
print()
PostOrder('A')
