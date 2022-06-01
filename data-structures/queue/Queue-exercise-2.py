from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

def binary_of_numbers():
    q=Queue()
    q.enqueue('0')
    for i in range(10):
        if q.front=='1':
            q.enqueue('0')
        if q.front=='0':
            q.enqueue('1')
        
    for i in range(q.size()):
        a=q.dequeue()
        print(a)
        
if __name__ == '__main__': 
    binary_of_numbers()    
            
        