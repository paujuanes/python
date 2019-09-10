class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myFunc(self):
        print('Hello, my name is ' + self.name + ' and I am ' + self.age + ' years old.')

print('Enter name:')
x = input()
print('Enter age:')
y = input()

p1 = person(x,y)
p1.myFunc()