class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary,age):
      self.name = name
      self.salary = salary
      self.age = age
      Employee.empCount += 1
