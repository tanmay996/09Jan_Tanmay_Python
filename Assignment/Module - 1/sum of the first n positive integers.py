# Write a python program to sum of the first n positive integers.
num = int(input("Enter a positive number : "))
val = 1
if num >= 0:
    for x in range(num):
        val = val + x   
        print(val)
else:
     print("Enter number should be positive integers...")
    