
class bankdetail:
    nm =  ""
    type = ""
    def getdetail(self):
        self.nm = input("Enter name :")
        accunt_type=int(input("Select account type \nEnter 1 for Current \nEnter 2 for Saving : "))
        if accunt_type == 1:
            self.type = "Current"
        elif accunt_type == 2:
            self.type = "Saving"
        else:
            self.type = "N/A"

class deposit:
    deposit = 0
    def deposit_amount(self):
        self.deposit = int(input("Enter Amount for deposit : "))
        if self.deposit < 2000:
            print("Minimum amount should be 2000")
        else:
            self.total = self.deposit

class withdraw(deposit):

    wthdrw = 0
    def wthdrw_amount(self):
        self.wthdrw = int(input("Enter Amount for Withdraw : "))
        if self.wthdrw >self.total:
            print("Insufficient Balance")
        else:
            self.total -= self.wthdrw
            print("Successfully withdraw",self.total)

class bank_statement(bankdetail,withdraw):
    def statement(self):
        print("-----Bank Statement-----")
        print("Account Name:",self.nm)
        print("Account type:",self.type)
        print("Account Balance:",self.total)

bank = bank_statement()
bank.getdetail()
bank.deposit_amount()
bank.wthdrw_amount()
bank.statement()

    
        