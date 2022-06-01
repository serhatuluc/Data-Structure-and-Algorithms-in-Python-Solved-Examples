
from gc import get_referents


class TreeNode():
    def __init__(self,data):
        self.data=data
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
      
    
        
    def print_tree(self,level):
        if self.get_level() >level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
        
                
                
                
    
    
def build_product_tree():
    root = TreeNode("Global")

    India = TreeNode("India")
    
    Gujarat = TreeNode("Gujarat")
    Gujarat.add_child(TreeNode("Ahmedabad"))
    Gujarat.add_child(TreeNode("Baroda"))
    
    Karnataka = TreeNode("Karnataka")
    Karnataka.add_child(TreeNode("Bagluru"))
    Karnataka.add_child(TreeNode("Mysore"))
    
    
    USA = TreeNode("USA")
    
    NewJersey= TreeNode("New Jersey")
    NewJersey.add_child(TreeNode("Princeton"))
    NewJersey.add_child(TreeNode("Trenton"))
    
    California= TreeNode("California")
    California.add_child(TreeNode("San Francisco"))
    California.add_child(TreeNode("Mountain View"))
    California.add_child(TreeNode("Palo Alto"))
    

  
    root.add_child(India)
    root.add_child(USA)
    India.add_child(Gujarat)
    India.add_child(Karnataka)
    USA.add_child(NewJersey)
    USA.add_child(California)
  
    return root
    
  

if __name__ == '__main__':
    rootnode=build_product_tree()
    rootnode.print_tree(1)
            
    
