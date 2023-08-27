class Dog:
     species = "Canis familiaris"
     def __init__(self, name, age):
         self.name = name
         self.age = age


buddy = Dog("Buddy", 9)
print(Dog)
print("id(Dog)",id(Dog)) # the same address

print(id(buddy))
#print(id(Buddy)) tak nie, nie tak
print("               ")


miles = Dog("Miles", 4)
print(Dog)
print(id(Dog)) # the same address

print(id(miles))
print("               ")


buddy.age = 10
print(buddy.age)

miles.species = "Felis silvestris"
print("miles.species",miles.species)

print("buddy.species", buddy.species)