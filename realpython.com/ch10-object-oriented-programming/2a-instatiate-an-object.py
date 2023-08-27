# 10.2 Exercises

# 1. Modify the Dog class to include a third instance attribute called coat_color, which stores the color of the dog's
# coat as a string.

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}.")