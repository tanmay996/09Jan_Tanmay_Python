eng = int(input("Enter Subject english marks :"))
math = int(input("Enter Subject math marks :"))
physics = int(input("Enter Subject phy marks :"))
chem = int(input("Enter Subject chem marks :"))

total = eng+math+physics+chem
PR =total/4
print("Total of four subject is",total)
print("PR is ",PR)
if  eng < 40 or math < 40 or physics <40 or chem <40:
    print("fails") 
elif PR >= 70:
    print("Dist")
elif PR >= 60:
    print("First class")
elif PR >= 50:
    print("Second class")
elif PR >= 40:
    print("Pass class")
else :
    print("Fail")



