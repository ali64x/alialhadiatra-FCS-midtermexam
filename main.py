from admin import *
from usermethods import *
admin = False
user = False
out_of_tries = False
exit = False
filepath="data.txt"
main_file = open(filepath, "r")


for i in range(4):
    UserName = input("User Name : ")
    password = input("password : ")
    if (UserName == 'admin' and password == 'admin123123') :
        admin=True
        break
    if searchfor(UserName,filepath):
        user = True
        break
    print("wrong username/password please try again !\n")
else :
    out_of_tries = True
    print("you have entered 5 wrong combinations please try again later")
while exit != True :
    if user == True : # handels user's interaction
        print("Hi",gender_of(UserName,filepath),UserName)
        print("1. Check my Salary")
        print("2. Exit")
        choice = input()
        if choice == '1' :
            print("your salary value is : ",salary_of(UserName,filepath))
        if choice == '2' :
            exit = True
    