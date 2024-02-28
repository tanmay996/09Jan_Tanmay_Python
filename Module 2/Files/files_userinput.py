data=open("userdata.txt","a")
num = int(input("Enter to to print table:"))
for x in range(1,11):
   
    data.write(str(f"{num} * {x} = {num*x} \n"))

    



