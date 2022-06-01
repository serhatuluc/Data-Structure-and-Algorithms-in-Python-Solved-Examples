class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
#this part is string BST(check binary.tree.py)      
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree = insert(None, "jadhesh.username", "jadhesh")
insert(tree, "biraj.username", "biraj")
insert(tree, "sonaksh.username", "sonaksh")
insert(tree, "aakash.username", "aakash")
insert(tree, "hemanth.username", "hemanth")
insert(tree, "siddhant.username", "siddhant")
insert(tree, "vishal.username", "vishal")

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value
        
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

def is_balanced(node):
    if node is None:
        return True, 0
 
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    print(balanced_l,balanced_r,height_r,height_l,height,balanced)
    return balanced, height

print(is_balanced(tree))


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None
    
    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)
    
    return root
