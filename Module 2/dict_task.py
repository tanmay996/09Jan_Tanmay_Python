# key id 
# n = int(input("Enter number of data to store : "))

# def userdata(id,name):
#     student ={
#         "id":id,
#         "name":name
#     }
    
#     print(student)
# for x in range(n):
#     stid = input("Enter id :")
#     stname = input("Enter name :")

#     userdata(stid,stname)

data = {}
key=["id","name"]

for x in range(len(key)):
    value = input(f"Enter {key[x]} : ")
    data[key[x]] =  value

print(data)