class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def insert(root, key):
    if not root:
        return AVLNode(key)
    
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    
    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)
        
    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)
        
    return root

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def sum_all_values(root):
    if root is None: #base case of recursion
        return 0
    return root.key + sum_all_values(root.left) + sum_all_values(root.right) #post order

root = None
keys = [5, 40, 15, 79, 46, 28, 95, 37, 17, 50, 68, 43, 86, 31, 83]

for key in keys:
    root = insert(root, key)


print("Sum of all values in the AVL-tree is:", sum_all_values(root))