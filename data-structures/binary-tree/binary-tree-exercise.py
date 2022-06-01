class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#node1 = TreeNode(1)
#node2 = TreeNode(2)
#node3 = TreeNode(3)
#node4 = TreeNode(4)
#node5 = TreeNode(5)
#node6 = TreeNode(6)
#node7 = TreeNode(7)
#node8 = TreeNode(8)

#tree=node2

#node2.left=node3
#node3.left=node1
#node2.right=node5
#node5.left=node3
#node5.right=node7
#node3.right=node4
#node7.left=node6
#node7.right=node8

def parse_tuple(data):
    #print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    
    return node

tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
#parse_tuple(tree_tuple)


#binary tree to tuple

def display_keys(node, space='\t', level=0):
    #print(node.key if node else None, level)
    
    # If the node is empty
    if node is  None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)   


tree =parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    
display_keys(tree,' ')

def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))
    
tree2 =parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))
print(traverse_in_order(tree2))


def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

print(tree_height(tree2))

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

print(tree_size(tree2))

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key

print(is_bst(tree2))

