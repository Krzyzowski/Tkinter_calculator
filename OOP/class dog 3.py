class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4)
print(miles.description())
miles.speak("Woof Woof")
print("               ")


print(miles.speak("Bow Wow"))
print(miles)

class Dog:
    # Leave other parts of Dog class as-is
    def __init__(self, name, age):
        self.name = name
        self.age = age



    # Replace .description() with __str__()
    def __str__(self):
        return f"{self.name} is {self.age} years old"

miles = Dog("Miles", 4)
print(miles)