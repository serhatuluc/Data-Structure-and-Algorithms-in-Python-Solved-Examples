#list
stock_prices=[]
with open ("datas.csv","r") as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        stock_prices.append([day,price])
print(stock_prices)

for element in stock_prices:
    if element[0]=="March":
        print(element[1])


#dictionary
stock_prices={}
with open ("datas.csv","r") as f:
    for line in f:
        tokens=line.split(',')
        day=tokens[0]
        price=float(tokens[1])
        stock_prices[day]=price
print(stock_prices)

print(stock_prices["March"])


#getting ASCI number of string in Hash Table
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
        found=False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx]=(key,val)
                found=True
                break
        if not found:
            self.arr[h].append((key,val))
                
    
    def __delitem__(self,key):
        h=self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0]==key:
                del self.arr[h][i]

    
    def get(self,key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]
        
        
    
t=HashTable()
t.add_("march 6",130)
t.add_("march 17",131)
print(t.get("march 6"))




    