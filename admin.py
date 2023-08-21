import datetime

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

def getlastid(filepath):# to get the last id from the file 
    with open(filepath, 'r') as data:
        lines = data.readlines()
        if lines:
            last_id = lines[-1].strip().split(',')[0]
            return last_id[3:]
    return "000"
def formatid(id):# to write the id in the propper format 
    if len(id) == 1:
        return 'emp00'+id
    elif len(id) == 2:
        return 'emp0'+id
    return 'emp'+id

def add_employee(name,gender,salary,filepath):
    timestamp = datetime.datetime.now().strftime('%y%m%d')#from https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
    intID = int(getlastid(filepath))+1
    ID = formatid(str(intID))
    with open(filepath,'a') as data :
        data.write(f"{ID},{name},{timestamp},{gender},{salary}\n")
    data.close()