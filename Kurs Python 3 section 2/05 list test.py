data = [0,1,2,3,4,5,6]
print("Długość listy:", len(data))

del data[2]
print("Długość listy - drugi el:", len(data))


if 3 in data:
    print("3 jest na liście")

for el in data:
    print("el + 2:",el + 2)

for el in data:
    print(el * 2)