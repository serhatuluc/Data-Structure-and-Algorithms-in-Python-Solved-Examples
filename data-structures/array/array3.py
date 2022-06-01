x=int(input("Please type a number"))

odds=[]

for i in range(1,x+1):
    if i%2!=0:
        odds.append(i)
print(odds)
    
    