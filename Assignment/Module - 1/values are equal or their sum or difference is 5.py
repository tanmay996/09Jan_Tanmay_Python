# Write a Python program that will return true if the two given integer 
# values are equal or their sum or difference is 5
num1 = int(input("Enter value 1 : "))
num2 = int(input("Enter value 2 : "))
diff = num1 - num2
sum = num1 + num2
if num1 == num2 or diff == 5 or sum == 5:
    print("True")
else :
    print("False")