n = int(input("Enter number for fibonacci :"))
a = 0
b = 1
print(a)
print(b)
for x in range(0,n):
    c = a + b
    print(c)
    a = b
    b = c
    