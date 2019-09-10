class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print('Welcome,', self.firstname, self.lastname, ', to the class of', self.graduationyear)

print('Enter your name:')
x = input()

print('Enter your surname:')
y = input()

print('Enter current year:')
z = input()
z = int(z)

s1 = Student(x, y, z)
s1.graduationyear = z + 1
s1.welcome()