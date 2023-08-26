class Dog:
    pass

print(Dog())
print(Dog())
a = Dog()
b = Dog()
print(a == b)
print(a)
print(b)

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
print(buddy.name)
print(buddy.age)
print(miles.name)
print(miles.age)
print(buddy.species)

buddy.age = 10
print(buddy.age)
miles.species = "Felis silvestris"
print(miles.species)

class Dog:
    species = "Canis familaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
print(miles.description())
print(miles.speak("Woof Woof"))
print(miles.speak("Bow Wow"))
print(miles)

class Dog:
    species = "Canis familaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4)
print(miles)