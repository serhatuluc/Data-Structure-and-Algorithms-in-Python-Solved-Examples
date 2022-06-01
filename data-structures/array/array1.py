from multiprocessing import Value


expenses={"Jaunuary":2200,
          "February":2350,
          "March":2600,
          "April":2130,
          "May":2190}
print(expenses["April"])

print("\n") 
#Total expenses
sum=0
for key in expenses:
   sum+=expenses[key]
print(sum)

print("\n") 
#Find spesific expense
length=0
for key in expenses:
    if expenses[key]==2000:
        print(key)
        break
    length+=1
    if length==len(expenses):
        print("no such expense")
print("\n")         
#Adding new expenses
expenses.update({"June":1980})
for i in expenses:
    print(i+":"+str(expenses[i]))
    
print("\n")    
#Update in dictionary    
expenses.update({"April":200})
for i in expenses:
    print(i+":"+str(expenses[i]))
