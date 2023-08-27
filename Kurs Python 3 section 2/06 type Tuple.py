
data = ("Ala", "Ola", "Kasia")
#data[0] = "Rafał" #TypeError: 'tuple' object does not support item assignment

names = data + ("Rafał",)
print(names)
print(len(names)) #4
print(type(names)) #<class 'tuple'>

numbers = 1, 2, 3
print(type(numbers)) #<class 'tuple'>

emptyTuple = ()
print(emptyTuple) #()
print(type(emptyTuple)) #<class 'tuple'>

print(names[1])
print(names[-1])
print(names[1:3])

cars = (("dodge","ford") , ("dontiac"))
print(cars[1][0])

if "ford" in cars[0]:
    print("Ford w krotce nr 1")

#del cars #wyrzuci błąd
print(cars)

tupleX3 = names * 3
print(tupleX3)