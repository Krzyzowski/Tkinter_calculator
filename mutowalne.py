f = 3.2
addr1 = id(f)

f = f + 2.5
addr2 = id(f)

print(addr1)
print(addr2)

print(addr1 == addr2)

listData = ['a', 'b']
addr3 = id(listData)

listData += ['c','d']
addr4 = id(listData)

print(addr3)
print(addr4)
print(addr3 == addr4)

def addToStr( string ):
    string += "!"
    print( "addToStr() string jako:" + string )

string = "Hello"

addToStr(string)
addToStr(string)
addToStr(string)

print("oryginalny:" + string)

def addToList( someList):
    someList.append(4)

listData = [2]

addToList(listData)
addToList(listData)
addToList(listData)

print("ostateczna lista: " + str(listData))

def addToList( someList ):
    print("someList przed zmianą: " + str(someList))
    someList = [30,40,50]
    print("someList po zmianie: " + str(someList))

listData = [2]

addToList(listData)

print("ostateczna lista: " + str(listData))