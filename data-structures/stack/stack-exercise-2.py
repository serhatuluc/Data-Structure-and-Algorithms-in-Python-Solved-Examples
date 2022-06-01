from collections import deque
stack=deque

from collections import Counter

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)
    
def is_balanced(s):
    stack=Stack()
    
    for ch in s:
        stack.push(ch)
        
    parant=[]
    while stack.size()!=0:
        a=stack.pop()
        if a=="(" or a=="{" or a=="[" or  a==")" or a=="}" or a=="]":
            parant.append(a)
    counts = Counter(parant)
    num_of_kapaliparantez=counts['('] 
    num_of_acikparantez=counts[')'] 
    num_of_kapalisusluparantez=counts['{'] 
    num_of_aciksusluparantez=counts['}'] 
    num_of_kapaliduvarparantez=counts['['] 
    num_of_acikduvarparantez=counts[']']  
    if num_of_kapaliparantez==num_of_acikparantez and num_of_kapalisusluparantez==num_of_aciksusluparantez and num_of_kapaliduvarparantez==num_of_acikduvarparantez:
        if parant[0]=="(" or parant[0]=="{" or parant[0]=="[" or parant[-1]==")" or parant[-1]=="}" or parant[-1]=="]":
            return False
        else: 
            return True
    else:
        return False

        
    
    

    

if __name__ == '__main__':
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
    