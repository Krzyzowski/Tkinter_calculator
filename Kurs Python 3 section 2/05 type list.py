
list = ["Ola", "Ania", 23, 99, "Rafał"]
print(type(list)) # <class 'list'>
print(list)

print(list[0])
print( len(list) )
print( list[4] ) #Rafał
print( list[len(list)-1] ) #Rafał

# print( list[5] ) # IndexError: list index out of range

print( list[-1] ) #Rafał
#print( list[-6] ) #IndexError: list index out of range

print( list[1:4] ) #['Ania', 23, 99]
print( list[2:] ) #[23, 99, 'Rafał']

list[0] = "Kasia"
print(list) #['Kasia', 'Ania', 23, 99, 'Rafał']

print(23 in list) # check 23
del list[2] # del 23
print(list) # ['Kasia', 'Ania', 99, 'Rafał']
print(23 in list) # check 23

print(99 in list) # check 99
print( "Rafał" in list )
print( "Ola" in list )

if "Ania" in list:
    print(" Ania jest w liście list ")
    print("Kolejny kod")

print("Dalszy kod")

for v in list:
    print(v)

data = [
    ["Daniel", "Rafał"],
    ["Kasia", "Ania"],
    ["Ola", "Adam"]
]

print(len(data))

print(data[1][0]) #Kasia
print(data[2][1]) #Adam







