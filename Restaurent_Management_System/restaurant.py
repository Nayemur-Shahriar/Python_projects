from menu import Menu

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.Employees=[]
        self.menu= Menu()

    def add_employee(self, employee):
        self.Employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def view_employees(self):

        if not self.Employees:
            print("No employees found.")
            return
        
        print("Employee List:")
        for emp in self.Employees:
            print(f"Name: {emp.name}, Email: {emp.email}, Phone: {emp.phone}, Address: {emp.address}, Age: {emp.age}, Designation: {emp.designation}, Salary: {emp.salary}")



