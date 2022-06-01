import threading
import time

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
    

q=Queue()
def place_order(list):
        for val in list:
            print("Placing order for:",val)
            q.buffer.appendleft(val)
            time.sleep(0.5)
    
        
def serve_order():
    try:
        while True:
            time.sleep(1)
            order=q.dequeue()
            print("Now serving: ",order)
            time.sleep(2)
    except IndexError:
        print("All of orders are served")  




if __name__ == '__main__':
    list = ['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=place_order,args=(list,))
    t2=threading.Thread(target=serve_order)
  
    t1.start()
    t2.start()
    