def addNumber(a,b,c):
    return a + b + c

def sumListElements(listData):
    if len(listData) == 0:
        print("Pusta lista!")
        return None
    result = 0
    for v in listData:
        result += v
    return result

print( sumListElements([]))
print( sumListElements([1,2,3]))

def printlist(listData):
    if len(listData) == 0:
        return
    for v in listData:
        print(v)

printlist([])
printlist([6,7,8])
