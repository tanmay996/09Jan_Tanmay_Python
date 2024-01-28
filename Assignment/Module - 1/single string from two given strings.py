# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
str1 = input("Enter string 1 :")
str2 = input("Enter string 2 :")
print(str1.replace(str1[0],str2[0])+" "+str2.replace(str2[0],str1[0]))