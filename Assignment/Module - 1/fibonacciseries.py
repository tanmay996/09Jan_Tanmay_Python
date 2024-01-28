# Write a Python program to get the Fibonacci series of given range
# 0 , 1 , 1, 2, 3, 5 , 8
num = int(input("Enter a range upto Fibonacci series: "))
val1 = 0
val2 = 1
print(val1)
print(val2)
for x in range(num-2):
    total = val1 + val2
    print(total)
    val1 = val2
    val2 = total


