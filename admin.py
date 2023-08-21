import datetime

def search_for(x,filepath):
    with open(filepath,'r') as file :
        for i in file:
            listofusers = i.strip().split(',')
            if x in listofusers :
                return True
        return None


def edit_name(new_name,id,filepath):
    new_lines = []

    with open(filepath, 'r') as file:
        for i in file:
            employee_data = i.strip().split(',')
            if employee_data[0] == id:
                employee_data[1] = new_name
                i = ','.join(employee_data) + '\n'
            else :
                print("ID doesn't exist !")
            new_lines.append(i)

    with open(filepath, 'w') as file:
        file.writelines(new_lines)
        
        

def edit_gender(new_gender,id,filepath):
    new_lines = []

    with open(filepath, 'r') as file:
        for i in file:
            employee_data = i.strip().split(',')
            if employee_data[0] == id:
                employee_data[3] = new_gender
                i = ','.join(employee_data) + '\n'
            else :
                print("ID doesn't exist !")
            new_lines.append(i)

    with open(filepath, 'w') as file:
        file.writelines(new_lines)



def edit_salary(new_salary,id,filepath):
    a=False
    new_lines = []

    with open(filepath, 'r') as file:
        for i in file:
            data = i.strip().split(',')
            if data[0] == id:
                data[4] = new_salary
                i = ','.join(data) + '\n'
                a =False
            new_lines.append(i)
            

    with open(filepath, 'w') as file:
        file.writelines(new_lines)



def getlastid(filepath):# to get the last id from the file 
    with open(filepath, 'r') as data:
        lines = data.readlines()
        if lines :
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
            data.write(f"{ID},{name},20{timestamp},{gender},{salary}\n")
    
# with the help of the following documentary https://stackoverflow.com/questions/72899/how-to-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python
# I was able to create the following funtion
def displayemployees(filepath):
    with open(filepath,'r') as file: 
        listofemployees=[]
        for i in file :
            data = i.strip().split(',')
            joining_date = datetime.datetime.strptime(data[2], '%Y%m%d')
            listofemployees.append({
                'name': data[1],
                'timestamp': joining_date,
            })
        sortedemployees = sorted(listofemployees, key=lambda x: x['timestamp'])
        for i in sortedemployees:
            print(f"Name: {i['name']}")

def remove_user(id, filepath):
    new_lines = []

    with open(filepath, 'r') as file:
        for line in file:
            employee_data = line.strip().split(',')
            if employee_data[0] != id:
                new_lines.append(line)

    with open(filepath, 'w') as file:
        file.writelines(new_lines)    

def find_name(id,filepath):
    with open(filepath, 'r') as file:
        for i in file:
            employee_data = i.strip().split(',')
            if employee_data[0] == id:
               return str(employee_data[1])
               break
        else :
           print("not found !")
           
def save_data(oldfile,newfile):
    with open(oldfile, 'r') as old_file:
        with open(newfile, 'w') as new_file:
             for content in old_file:
                new_file.write(content)