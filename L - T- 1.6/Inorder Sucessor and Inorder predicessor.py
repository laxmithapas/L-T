class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_pre_suc(root, key):
    pre = None
    suc = None
    current = root

    while current:
        if current.key < key:
            pre = current
            current = current.right
        elif current.key > key:
            suc = current
            current = current.left
        else:
            # Find predecessor in left subtree
            if current.left:
                temp = current.left
                while temp.right:
                    temp = temp.right
                pre = temp
            # Find successor in right subtree
            if current.right:
                temp = current.right
                while temp.left:
                    temp = temp.left
                suc = temp
            break
    return pre, suc

# Example usage:
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

key = 65
pre, suc = find_pre_suc(root, key)
print("Predecessor:", pre.key if pre else None)
print("Successor:", suc.key if suc else None)
