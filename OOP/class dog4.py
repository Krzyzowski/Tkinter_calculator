class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Replace .description() with __str__()

    def __str__(self):
        return f"{self.name} is {self.age} years old"

miles = Dog("Miles", 4)

print(miles)