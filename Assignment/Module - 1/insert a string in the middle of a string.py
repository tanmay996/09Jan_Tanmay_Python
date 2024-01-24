# Write a Python function to insert a string in the middle of a string.
str1 =input("Enter a string : ")
str1= str1.split()
result=""
if len(str1) > 1:
    middle = int(len(str1)/2)
    add = input("Entet a middle string : ")
    add = add.split()
    str1 = str1[:middle] + add +str1[middle:]
    for x in range(len(str1)):
        result = result + " " +str1[x]
    print(result)
else :
    print("String must be more than 1 word")