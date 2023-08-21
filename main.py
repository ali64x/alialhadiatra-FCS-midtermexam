from admin import *
from usermethods import *
admin = False
user = False
out_of_tries = False
exit = False
male_count , female_count =0,0
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
    if admin == True : # handels admin's interaction 
        print("1. Display Statistics") 
        print("2. Add an Employee") 
        print("3. Display all Employees") 
        print("4. Change Employee’s Salary") 
        print("5. Remove Employee") 
        print("6. Raise Employee’s Salary") 
        print("7. Exit")
        choice = input()
        if choice == '1':
            for i in main_file:
                gender = i.strip().split(',')
                if gender[3] == 'male':
                    male_count += 1
                else :
                    female_count += 1
            print(f"There are {male_count} male employees , and {female_count} female employees in the company")
        if choice == '2':
            name = input("USER NAME : ")
            gender = input("GENDER : ")
            salary = input("SALARY : ")
            add_employee(name,gender,salary,filepath)