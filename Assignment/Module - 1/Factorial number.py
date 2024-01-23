# 5! = 5 *  4 * 3 * 2 * 1
# fact = 5
# for x in range(1,5):
#     fact = fact * x
#     print(fact)


# val = int(input("Enter a number for factorial : "))
# for x in range(1,val):
#     total = val
#     val*=x
#     print(f"{total} * {x} = {val}")
# print(f"factoiral of ")
val = int(input("Enter a number for factorial : "))
fact = val
for x in range(1,val):
   fact *= x
   
print(f"Factorial of {val}! is {fact}")
