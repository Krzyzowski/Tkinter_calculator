
data = (100, 200, 300, 400, 500, 600)
print(type(data))

expenses = 100, 200, 300, 400, 500, 600
print(type(expenses))

num = 0
for v in expenses:
    num = num + v

print("Suma wydatków:", num)