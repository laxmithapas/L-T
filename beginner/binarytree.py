class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree(node):
    if node is None:
        return
    print(f"{node.value}")
    if node.left or node.right:
        print("     /  \\")
        left_val = str(node.left.value) if node.left else " "
        right_val = str(node.right.value) if node.right else " "
        print(f"    {left_val}   {right_val}")

# Creating nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)

# Print the simple tree
print("Simple Binary Tree:")
print_tree(root)
