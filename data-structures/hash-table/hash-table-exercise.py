#part1

#nyc_weather=[]
#with open ("datas.csv","r") as f:
#    for line in f:
#        tokens=line.split(',')
#        day=tokens[0]
#        temperature=float(tokens[1])
#        nyc_weather.append(temperature)
#print(nyc_weather)
#
#print(sum(nyc_weather[0:7])/7)
#print(max(nyc_weather))

#----------------------------------------------------------------------------------------------------------------
#part2

#nyc_weather=[]
#with open ("datas.csv","r") as f:
#    for line in f:
#        tokens=line.split(',')
#        day=tokens[0]
#        temperature=float(tokens[1])
#        nyc_weather.append([day,temperature])
#nyc_weather=dict(nyc_weather)
#print(nyc_weather)
#print(nyc_weather["Jan 4"])
#print(nyc_weather["Jan 9"])

#---------------------------------------------------------------------------------------------------------------
#part3

#words_poem=[]
#with open('poem.txt','r') as file:
#   
#    # reading each line    
#    for line in file:
#   
#        # reading each word        
#        for word in line.split():
#            words_poem.append(word)
#            # displaying the words           
#print(words_poem)
#
#string='I'
#count=0
#for i in range(len(words_poem)):
#    if words_poem[i]==string:
#        count+=1
#print(string+":"+str(count))

#------------------------------------------------------------------------------------------------------------
#part3(professional solution)

#word_count = {}
#with open("poem.txt","r") as f:
#    for line in f:
#        tokens = line.split(' ')
#        for token in tokens:
#            token=token.replace('\n','')
#            if token in word_count:
#                word_count[token]+=1
#            else:
#                word_count[token]=1
#print(word_count)
 
#--------------------------------------------------------------------------------------------------------------


