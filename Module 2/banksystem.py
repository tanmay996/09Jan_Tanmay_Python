# account_name = input("Enter your account name : ")
# account_number =int(input("Enter your account number : "))
# acc_type = int(input("Enter 1 for Saving \nEnter 2 for current : "))
# total_amount = int(input("Enter amount for deposite : "))

# if acc_type == 1:
#         account_type = "saving"
# else:
#         account_type = "cuurent"

# def bankdata(account_name,account_number,account_type,total_amount):
#         print("Account Holder :",account_name)
#         print("Account Number :",account_number)
#         print("Account Type :",account_type)
#         print("Balance available :",total_amount)

# if total_amount < 2000:
#     print("Minimum balance should be deposit 2000")
# else:
#     withdraw_amount =int(input("Enter amount for withdraw : "))
   

#     if total_amount >= withdraw_amount:
#             total_amount-=withdraw_amount
#             print("Succefully withdraw : ",total_amount)
#             bankdata(account_name,account_number,account_type,total_amount)
    
#     else:
#              print("Insufficiant balance")




















account_name:str
account_number:int
account_type:str
def account_detail():
    account_name = input("Enter your account name : ")
    account_number =int(input("Enter your account number : "))
    acc_type = int(input("Enter 1 for Saving \nEnter 2 for current : "))
    if acc_type == 1:
        account_type = "saving"
    else:
        account_type = "cuurent"

account_detail()
print(account_name)

# def deposit():
#     total_amount = int(input("Enter amount for deposite : "))
#     if total_amount < 2000:
#      print("Minimum balance should be deposit 2000")
#     else:
#         withdraw()

# def withdraw():
        
#         withdraw_amount =int(input("Enter amount for withdraw : "))

#         if total_amount >= withdraw_amount:
#             total_amount-=withdraw_amount
#             print("Succefully withdraw : ",total_amount)
          
    
#         else:
#              print("Insufficiant balance")




