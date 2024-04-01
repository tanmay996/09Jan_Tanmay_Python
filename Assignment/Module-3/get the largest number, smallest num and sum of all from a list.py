lst = [5,4,2,1,6,9,8]
res = 0


def listask():
    global res
    lst.sort()
    print("Largest number is : ",lst[-1])
    print("Smallest number is : ",lst[0])
    for x in range(0,len(lst)):
        res+=lst[x]
    print("sum of all from list is : ",res)

listask()