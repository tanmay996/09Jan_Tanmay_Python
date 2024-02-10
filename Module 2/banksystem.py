accunt_no=""
holder_name=""
type=""
total=0
wthdrw=0



def detail():
    global accunt_no, holder_name, type
    accunt_no = input("Enter Your account number : ")
    holder_name = input("Enter Your account name : ")
    accunt_type=int(input("Select account type \nEnter 1 for Current \nEnter 2 for Saving : "))
    if accunt_type == 1:
        type = "Current"
    elif accunt_type == 2:
        type = "Saving"
    else:
        type = "N/A"

def deposit():
    global total
    deposit = int(input("Enter Amount for deposit : "))
    if deposit < 2000:
        print("Mnimum amount shoul be 2000")
    else:
        total = deposit
    

def withdraw():
    global total,wthdrw
    wthdrw = int(input("Enter Amount for Withdraw : "))
    if wthdrw > total:
        print("Insufficient Balance")
    else:
        total -= wthdrw



def statements():
    global accunt_no, holder_name, type, total
    print("Your Account number : ",accunt_no)
    print("Your Account name : ",holder_name)
    print("Your Account type : ",type)
    print("Your Bank Balance : ",total)

detail()
deposit()
withdraw()
statements()



