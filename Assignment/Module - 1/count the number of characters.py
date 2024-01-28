# WWrite a Python program to count the number of characters (characterfrequency) in a string
# str = "Hello world"
# output = H = 1,e=1 ,l=3 ,w=1,o=2,r=1,d=1

str1 = input("Enter a string for calculate character frequency : ")
for x in range(len(str1)):
    print(str1[x] ,str1.count(str1[x]))
