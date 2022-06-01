
class TreeNode():
    def __init__(self,data,designation):
        self.data=data
        self.designation=designation
        self.children=[]
        self.parent=None
     
        
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
            
            
        
    def add_child(self,child):
        self.children.append(child)
        child.parent=self
      
        
    def add_design(self,designat):
        self.designation.append(designat)
        designat.parent=self
        
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.designation)
        if self.children:
            for child in self.children:
                child.print_tree()
    
def build_product_tree():
    root = TreeNode("Nilupul","CEO")

    Chinmay = TreeNode("Chinmay","CTO")
    Chinmay.add_child(TreeNode("Aamir","Application Head"))
    
    
    Vishwa = TreeNode("Vishwa","Infrastructure Head")
    Vishwa.add_child(TreeNode("Dahaval","Clud Manager"))
    Vishwa.add_child(TreeNode("Abhijit","App Manager"))
    
    
    Gels = TreeNode("Gels","HR Head")
    Gels.add_child(TreeNode("Peter","Recruitment Manager"))
    Gels.add_child(TreeNode("Waqas","Policy Manager"))
    

  
    root.add_child(Gels)
    root.add_child(Chinmay)
    Chinmay.add_child(Vishwa)
  
    
    
    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
            
    
        
        
        
    