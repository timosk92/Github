class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age



newEmployee = input("Name?: ")
employee = Employee(newEmployee,26)

print (str(employee.name))
print (str(employee.age))
print(isinstance (employee,Employee))
