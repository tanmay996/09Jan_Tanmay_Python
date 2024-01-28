# Write a Python function that takes a list of words and returns the length
# of the longest one
str1 = input("Enter a string : ")
str1 = str1.split()
for x in range(1,len(str1)):
    if len(str1[0]) < len(str1[x]):
        str1[0] = str1[x]
print(str1[0])