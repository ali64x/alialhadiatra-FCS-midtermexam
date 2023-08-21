from admin import *
from usermethods import *
admin = False
user = False
out_of_tries = False
exit = False
male_count , female_count =0,0
temp_file="temp.txt"
main_file = "data.txt"
while out_of_tries != True :
    save_data(main_file,temp_file)
    for i in range(4):
        admin=False
        user=False
        UserName = input("User Name : ")
        password = input("password : ")
        if (UserName == 'admin' and password == 'admin123123') :
            admin=True
            exit=False
            break
        if search_for(UserName,temp_file):
            user = True
            exit=False
            break
        print("wrong username/password please try again !\n")
    else :
        out_of_tries = True
        print("you have entered 5 wrong combinations please try again later")
        break
    while exit != True :
        if user == True : # handels user's interaction
            print("Hi",gender_of(UserName,temp_file),UserName)
            print("1. Check my Salary")
            print("2. Exit")
            choice = input()
            if choice == '1' :
                print("your salary value is : ",salary_of(UserName,temp_file))
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
                male_count=0
                female_count=0
                with open(temp_file,'r') as file:
                    for i in file:
                        gender = i.strip().split(',')
                        if gender[3] == 'male':
                            male_count += 1
                        else :
                            female_count += 1
                print(f"There are {male_count} male employees , and {female_count} female employees in the company")
            if choice == '2':
                name = input("USER NAME : ")
                if not search_for(name,temp_file):
                    gender = input("GENDER : ")
                    salary = input("SALARY : ")
                    add_employee(name,gender,salary,temp_file)
                    print('\nDone !\n')
                else : 
                    print("user already exist !")
            if choice == '3':
                displayemployees(temp_file)
                print('\nDone !\n')
            if choice == '4' :
                id = input("please enter the employee's ID : ")
                if search_for(id,temp_file) :
                    newsalary = input("New salary : ")
                    edit_salary(newsalary,id,temp_file)
                    print('\nDone !\n')
                else:
                    print("ID doesn't exist !")
            if choice == '5':
                id = input("please enter the employee's ID : ")
                if search_for(id,temp_file) :
                    remove_user(id,temp_file)
                    print('\nDone !\n')
                else :
                    print("ID doesn't exist !")
            if choice == '6' :
                id = input("Please enter the employee's ID : ")
                if search_for(id,temp_file) :
                    raise_percent = int(input("Enter the raise percentage : "))
                    old_salary=int(salary_of(find_name(id,temp_file),temp_file))
                    newsalary = ((old_salary* raise_percent)/100)+old_salary
                    edit_salary(str(newsalary),id,temp_file)
                    print("\nDone !\n")
                else:
                     print("ID doesn't exist !")
            if choice == '7':
                save_data(temp_file,main_file)
                print('\nSaved !\n')
                exit = True
            