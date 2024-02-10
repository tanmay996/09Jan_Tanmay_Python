

def getdata(acno,acnm):
    return acno,acnm

def statement():
    x=getdata(1,'Sanket')
    print("No:",x[0])
    print("Name:",x[1])


statement()