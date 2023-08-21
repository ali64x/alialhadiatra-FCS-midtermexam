def gender_of(username,filepath):
    with open(filepath,"r") as userdata:
        for i in userdata:
            gender = i.strip().split(',')
            if gender[1] == username:
                if gender[3]=='male':
                    return "Mr."
                return "Mrs."
    return None

def salary_of(username,file_path):
    with open(file_path,"r") as userdata:
        for i in userdata:
            salarylist = i.strip().split(',')
            if salarylist[1] == username:
                return str(salarylist[4])
    return None