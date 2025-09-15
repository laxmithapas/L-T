class Node:
    def _init_(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
        return root
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        preorder(root.left)
        print(root.val, end=' ')
        preorder(root.right)

root = None
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    root = insert(root, v)
inorder(root)