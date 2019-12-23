class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def get_biggest_number(*nums):
    return max(*nums)

dog1 = Dog("Nikola", 2)
dog2 = Dog("Tesla", 4)
dog3 = Dog("Newton", 7)

oldest = get_biggest_number(dog1.age, dog2.age, dog3.age)

print(f'The oldest dog is {oldest} years old.')