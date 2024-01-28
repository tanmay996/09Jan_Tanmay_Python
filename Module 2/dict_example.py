data={
    "id":101,
    "name":"tanmay",
    "age":"25"
}
print(data)
# print(data["age"])

# print(data.keys())
# print(data.values())


# Else statement will execute because it will check Key not value 
# if "tanmay" in data:
#     print("yes")
# else:
#     print("Noooo")


#To check value in dictionary
# if "tanmay" in data.values():
#     print("yes")
# else:
#     print("Noooo")

#both are same 
# data.pop("age")
# del data["age"]
# print(data)

# data.clear()
# print(data)


# del data
# print(data)

newdata = data.copy()
print("new data",newdata)