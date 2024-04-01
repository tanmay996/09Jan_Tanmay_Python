list =[1,2,3,4,5,6,7,8,9,11,22,12,25,16]
newlist = list[0:6] + list[len(list) - 4 : len(list)]
generatedlist = []
for x in newlist:
    for y in range(1,x):
        if y * y == x:
            generatedlist.append(x)


print(list)
print(generatedlist)