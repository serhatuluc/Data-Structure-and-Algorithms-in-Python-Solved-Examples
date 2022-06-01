#Rotated Lists/Definition of problem:
    #Rotating list means removing last element and adding it
    #before first element.
#Input-output formats:
    #The function will take a sorted list of number as input
    #and will give rotated list as output. 
    #Input:[0,2,3,4,5,6,9] (increasing order),number of rotation
    #Query:number of rotation
    #Output:[5,6,9,0,2,3,4]
#Test cases: 
    #tests=[]
    #tests.append({'input':{'list':[2,5,9,12,16,18,20,23,27,30],'num_rot':3},'output':[23,27,30,2,5,9,12,16,18,20]})
    #tests.append({'input':{'list':[2,5,9,12,16,18,20,23],'num_rot':5},'output':[12,16,18,20,23,2,5,9]})
    #tests.append({'input':{'list':[2,5,9,12,16,18,20,23],'num_rot':0},'output':[2,5,9,12,16,18,20,23]})
    #tests.append({'input':{'list':[2,5,9,12,16,18,20,23],'num_rot':1},'output':[23,2,5,9,12,16,18,20]})
    #tests.append({'input':{'list':[2,5,9,12,16,18,20,23],'num_rot':7},'output':[5,9,12,16,18,20,23,2]})
    #tests.append({'input':{'list':[],'num_rot':2},'output':[]})
    #tests.append({'input':{'list':[2],'num_rot':2},'output':[2]})
#Brute force solution:
    #By using indexes the position of elements can be changed easily.add()

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
       

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self):
        itr=self.head
        while itr.next:
            itr=itr.next
        data1=itr.val     
        node = ListNode(data1, self.head)
        self.head = node
        
            
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    def remove_at(self):

        count = 0
        itr = self.head
        while itr:
            if count == self.get_length() - 2:
                itr.next = None
                break

            itr = itr.next
            count+=1
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.val)+' --> 'if itr.next else str(itr.val) 
            itr = itr.next
        print(llstr)
    
    def insert_at_end(self, val):
        if self.head is None:
            self.head = ListNode(val, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = ListNode(val, None)
        
        itr=self.head
        while itr:
            itr=itr.next
        return itr
    

    
    def insert_values(self,list):
            self.head=None
            for val in list:
                self.insert_at_end(val)
                
    
    def rotateRight(self,num_rot):
        i=0
        while i<num_rot:
            self.insert_at_begining()
            self.remove_at()
            i+=1   
        
    
ll=LinkedList()
#ll.insert_at_end(2)
ll.insert_values([2,5,9,12,16,18,20,23,27,30])
ll.rotateRight(3)
#ll.get_length()
#ll.insert_at_begining()
ll.print()
    