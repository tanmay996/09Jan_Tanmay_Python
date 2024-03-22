import tkinter

screen = tkinter.Tk()
screen.title("Calculator")
lbl1 = tkinter.Label(text="Enter value 1 :").grid(row=0,column=0)
input1 = tkinter.Entry()
input1.grid(row=0,column=2)
lbl2 = tkinter.Label(text="Enter value 2 :").grid(row=1,column=0)
input2 = tkinter.Entry()
input2.grid(row=1,column=2)

def btnP():
    print("Addition is :")
   
# def btnM():
  
# def btnMult():
    

# def btnD():
   

tkinter.Button(command= btnP ,text='+').grid(row=2,column=0)
# tkinter.Button(command = btnM , text='-').grid(row=2,column=1)
# tkinter.Button(command = btnMult , text='*').grid(row=2,column=2)
# tkinter.Button(command = btnD , text='/').grid(row=2,column=3)


screen.mainloop()