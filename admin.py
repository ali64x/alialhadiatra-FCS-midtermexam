class admin_control:
    def __init__(self, file):
        self.file = file

    def searchfor(self, x):
        with open(self.file, 'r') as f:
            for i in f:
                employee_data = i.strip().split(',')
                if employee_data[1] == x:
                    return employee_data
        return None

    def edit_name(self, old_name, new_name):
        pass
    
    def edit_id(self, old_id, new_id):
        pass
    
    def edit_gender(self, old_gender, new_gender):
        pass
    
    def edit_salary(self, old_salary, new_salary):
        pass