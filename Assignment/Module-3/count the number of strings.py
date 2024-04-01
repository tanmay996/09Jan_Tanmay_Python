strlist = ["php" , "mom" , "hello" , "world" , "mam"]
count = 0

def countstr(list,count):
    for x in range(0,len(list)):
        temp = list[x]
        if temp[0] == temp[-1]:
            count += 1
    print(count)
    
countstr(strlist,count)