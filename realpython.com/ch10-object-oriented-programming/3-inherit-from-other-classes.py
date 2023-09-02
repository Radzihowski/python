# 10.3 Exercises

# 1. Create a GoldenRetriver class that inherits from the Dog class.
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self):
        return f"{self.name} is {self.age} years old"

    def __init__(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriver(Dog):
    def __int__(self, sound="Bark"):
        return super().speak(sound)

print(GoldenRetriver)