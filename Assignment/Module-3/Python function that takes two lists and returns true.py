list1 = [1,2,4]
list2 = [5,7,8,9,0,1]

def checklst(lst1,lst2):
    result = "False"
    for x in lst1:
        for y in lst2:
            if x == y:
                result = "False"
    print(result)
    

checklst(list1,list2)
