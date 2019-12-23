#Parent class
class Pets:
    dogs = []
    
    def __init__(self, dogs):
        self.dogs = dogs

# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return f'{self.name} is {self.age}.'

    # instance method
    def speak(self, sound):
        return f'{self.name} says {sound}.'
    
    #instance method
    def eat(self):
        self.is_hungry = False

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}.'

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}.'

# - - - - - - - - - - - - -
#Creating instances of dogs
my_dogs = [
    Bulldog('Tom', 6),
    RussellTerrier('Fletcher', 7),
    Dog('Larry', 9)
    ]

#Instantiating the Pets class
my_pets = Pets(my_dogs)

#Output
print(f'I have {len(my_pets.dogs)} dogs.')
for dog in my_pets.dogs:
    dog.eat()
    print(dog.description())
print(f"And they're all {Dog.species}s, of course.")

#Checking if any dog is hungry
for dog in my_pets.dogs:
    print(f'{dog.name} is hungry!' if dog.is_hungry else f'{dog.name} is not hungry.')

#Outputting whether all dogs are hungry or not
hungry = [dog.is_hungry for dog in my_pets.dogs]
print('My dogs are hungry!' if all(hungry) else 'My dogs are not hungry.')
