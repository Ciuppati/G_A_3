import pandas as pd

class Employee:
    def __init__(self, name):
        self.name = name
        self.work_details = {}

    def add_work_day(self, day, work_type, hours):
        if work_type not in self.work_details:
            self.work_details[work_type] = [0] * 31
        self.work_details[work_type][day-1] = hours

    def to_dict(self):
        return {
            "nome": self.name,
            "lavorate": self.work_details
        }

def convert_employee_data(file_path):
    # Load the provided Excel file
    df = pd.read_excel(file_path)

    # Strip leading and trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Fill down the employee names
    df['Nominativo'].fillna(method='ffill', inplace=True)

    # Create a dictionary to store Employee objects
    employees = {}

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        name = row['Nominativo']
        if name not in employees:
            employees[name] = Employee(name)

        work_type = row['Causale']
        for day in range(1, 32):
            day_str = str(day)
            if day_str in row and not pd.isna(row[day_str]):
                employees[name].add_work_day(day, work_type, row[day_str])

    # Convert the dictionary to a list of Employee objects
    employee_list = [emp.to_dict() for emp in employees.values()]
    
    return employee_list

# Example usage
#file_path = 'PRESENZE REWORK.xlsx'
#employee_data = convert_employee_data(file_path)

# Display the first few employee dictionaries
#print(employee_data[:5])

def get_employee(employee_list, name):
    for employee in employee_list:
        if employee['nome'].lower() == name.lower():
            return employee
    return None