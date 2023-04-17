num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int( input("Podaj liczbę startową:"))
        reset = False

    operation = input("co chcesz zrobić" + str(calcOperations) + " lub exit jeśli koniec lub reset: ")
    if operation == "exit": break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperations:
        print("błędna operacja")
        continue

    secondNum = int(input("Druga liczba...:"))

    if operation == "+":
        result = num + secondNum

    if operation == "-":
        result = num - secondNum

    if operation == "*":
        result = num * secondNum

    if operation == "/":
        result = num / secondNum

    if operation == "**":
        result = num ** secondNum

    print("Wynik" + str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))

    num = result
    result = None