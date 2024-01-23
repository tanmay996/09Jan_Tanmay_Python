id = input("Enter your id : ")

if id.isdigit() == True and len(id) == 4:
    name = input("Enter your name : ")
    if name.isalpha() == True:
        email = input("Enter your email : ")
        if email.islower() == True:
            passw = input("Enter your pass : ")
            copassw = input("Enter your confirm password : ")
            if(passw == copassw):
                print("Form Submit successfully")
            else:
                print("password must same")
        else :
            print("Email must be in lower case")
    else :
        print("Name should be alphabtic")
   
else :
    print("Id must be digits and not more 4 digit")



  
       