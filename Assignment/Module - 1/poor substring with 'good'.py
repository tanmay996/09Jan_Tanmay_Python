# Write a Python program to find the first appearance of the substring
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
# whole 'not'...'poor' substring with 'good'. Return the resulting string

str1 = "Hello! not python is  so poor language"
loc1 = str1.find("not")
loc2 = str1.find("poor")
print(str1.replace(str1[loc1:loc2+4],"good"))
      

    
   
    
