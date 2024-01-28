n = int(input("Enter no. of element to insert :"))
data={}
for x in range(n):
    k = input(f"Enter key {x +1 } : " )
    v = input(f"Enter value for key {x + 1} : ")
    data[k] = v
print(data)