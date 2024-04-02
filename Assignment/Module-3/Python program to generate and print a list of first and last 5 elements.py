list = []
generatelist =[]

for x in range(1,31):
    list.append(x)

newlist = list[0:5] + list[-5:]
for x in range(0,len(newlist)):    
    generatelist.append(newlist[x] ** 2)

print(generatelist)



    