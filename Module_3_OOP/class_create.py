class student:
    id=101
    name="tanmay"
    def getdata(self):
        print("this is gatedata")
    def getsum(self,a,b):
        print(f"Addition is : {a+b}",)
st = student()
print(st.name)
st.getdata()
st.getsum(5,4)