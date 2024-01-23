# Write a Python function to reverses a string if its length is a multiple of 4.
str1 = input("Enter a string for reverse : ")
result = ""
print(len(str1))
if len(str1) % 4 == 0:
    for x in range(len(str1)-1 , -1 , -1):
        result+=str1[x]
    print(result)
else:
    print("Cannot reverse")
       