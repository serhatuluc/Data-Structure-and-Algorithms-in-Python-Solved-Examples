class BinarySearchTree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
    def add_child(self,data):
        if data==self.data:
            return
        
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
                
        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)
                
    def search(self,data):
        if data==self.data:
            return True
        
        
        if data<self.data:
            if self.left:
                self.left.search(data)
                
            else:
                return False
        
        if data>self.data:
            if self.right:
                self.right.search(data)
                
            else:
                return False
        
        
    def inorder_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.inorder_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements+=self.right.inorder_traversal()
            return elements
            
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
        
    def preorder_traversal(self):
        elements=[]
        
        elements.append(self.data)
        
        if self.left:
            elements+=self.left.inorder_traversal()
        
        if self.right:
            elements+=self.right.inorder_traversal()
            return elements
        
    def pastorder_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.inorder_traversal()
        
        
        if self.right:
            elements+=self.right.inorder_traversal()
            return elements
        
        elements.append(self.data)
        
        
    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left.delete()
        elif val>self.data:
            if self.right:
                self.right.delete()
            
        else:
            if self.left and self.right is None:
                return None
            if self.right is None:
                self.right.delete()
            if self.left is None:
                self.left.delete()
                
        #min_val=self.right.find_min()
        #self.data=min_val
        #self.right = self.right.delete(min_val)
        
        max_val=self.left.find_max()
        self.data=max_val
        self.left = self.left.delete(max_val)
                
        
        
        
            
        
            
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root=BinarySearchTree(elements[0])
    for i in range(len(elements)):
        root.add_child(elements[i])
        
    return root


        

    
    
        
    
        
                
                