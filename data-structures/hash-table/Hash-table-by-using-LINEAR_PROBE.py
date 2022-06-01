class HashTable:
    def __init__(self):
        self.Max=10
        self.arr=[[] for i in range(self.Max)]
    
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%10
    
    def add_(self,key,val):
        h=self.get_hash(key)
        count=0
        while True:
            if len(self.arr[h])==1:
                h=(h+1)%10
                count+=1
                if count==10:
                    raise Exception("Hash table is full")
            else:
                break    
        self.arr[h].append((key,val))

    def update(self,key,val):
        h=self.get_hash(key)
        found=True
        while found:
            for idx, element in enumerate(self.arr[h]):
                if element[0]==key:
                    self.arr[h][idx]=(key,val)
                    found=False  
                    break 
                h=(h+1)%10
        
        
    def __delitem__(self,key):
        h=self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][index]

    
    def get(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
     


       
t=HashTable()
t.add_("march 6",130)
t.add_("march 17",131)
t.add_("march 6",130)

t.update("march 17",132)
#print(t.get("march 6")) 
print(t.arr) 


