from admin import *
from usermethods import *
main_file = open("data.txt", "r")
UserName = input("User Name : ")
password = input("password : ")
admin = False
user = False
out_of_tries = False
while out_of_tries != True :
    for i in range(5):
        if (UserName == 'admin' and password == 'admin123123') :
            admin=True
            break
        if (UserName in main_file and password == None):
           user = True
           break
        print("wrong username/password please try again !\n")
        UserName = input("User Name : ")
        password = input("password : ")
    else :
        out_of_tries = True
        print("you have entered 5 wrong combinations please try again later")
if user == True :
    print("Hi ",gender_of(UserName),UserName)
    print("1. Check my Salary")
    print("2. Exit")
    choice = input()
    if choice == '1' :
        print("your salary value is : ",salary_of(UserName))