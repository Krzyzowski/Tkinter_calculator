class Dog:
    pass

print(Dog)

a = Dog()
print("a",a)

print("Dog after a",Dog())

b = Dog()
print("Dog b", Dog())

print("b",b)

print("Dog after b", Dog())

a == b
print("a == b", a == b)
print("              ")
print("a == Dog()", a == Dog())
print("              ")
print("b == Dog()", b == Dog())
print("              ")
print("Dog() == Dog()", Dog() == Dog())



