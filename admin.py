def searchfor(x,filepath):
    with open(filepath, 'r') as f:
        for i in f:
            employee_data = i.strip().split(',')
            if employee_data[1] == x:
                return employee_data
    return None

def edit_name(old_name, new_name):
    pass

def edit_id(old_id, new_id):
    pass

def edit_gender(old_gender, new_gender):
    pass

def edit_salary(old_salary, new_salary):
    pass