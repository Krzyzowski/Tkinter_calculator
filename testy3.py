def findLargest(num1, num2):
    if (num1 > num2):
        print("num1 jest większe:", num1)
        return num1
    elif (num2 > num1):
        print("num2 jest większe", num2)
        return num2
    else:
        print("Obie liczby są równe o wartości:", num1)
        return num1

v1 = findLargest(3, 10)
print("Wynik wywołania:", v1)

v2 = findLargest(12, 7)
print("wynik wywołania:",v2)