list = [1,2,3,4,3,2,2,5,6,8,1,2]
temp = []
def generatedlist(lst,temp):
    for x in lst:
        if x in temp:
            pass
        else:
            temp.append(x)
    
    print(temp)
            

generatedlist(list,temp)

