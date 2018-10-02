import Class


def displaySalary(self):
      print( "Name: ", self.name,  ", Salary: ", self.salary)

def displayAge(name):
        print ("Checking "+name+"'s' records...")


def updateEmployee(newEmployee):
    name= input ("Name?: ")
    wage= input ("Wage?: ")
    age= input ("Age?: ")
    newEmployee.age = age
    newEmployee.wage = wage
    newEmployee.name = name
    print (newEmployee.name + " added")

print ("\n\n\nObject Oreintated Database by Tim Kelly\n\n\n")
employee = [10]
exit = 0
while exit == 0 :
    newCommand = input ("Command?: ")

    if newCommand in ('new employee', 'New Employee'):
        employee[0] = Class.Employee("",0,0)
        updateEmployee(employee[0])

    if newCommand in ('Age', 'age'):
        print ("Age Lookup")
        print("-------")
        name = input ("Employee Name?: ")
        displayAge(newEmployee)

    if newCommand in ('Total', 'total'):
        print ("Total Employees: " + str(Class.Employee.empCount))

    if newCommand in ('Exit','exit'):
        exit = 1
