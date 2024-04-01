list = [1,2,4,5,6,7,2,1,3,2,5,3]
temp = []
for x in range(0,len(list)-1):
    if list[x] in temp:
        pass
    else:
        temp.append(list[x])
print(temp)


