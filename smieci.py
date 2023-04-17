def addToStr( string):
    string += "!"
    print( "addToStr() string jako:" + string )

string = "Hello"

print("oryginalny: " + string)

v = addToStr(string)

addToStr(string)

def addToList( someList ):
    someList.append(43)
    print(someList)

listData = [2]

addToList(listData)
addToList(listData)
addToList(listData)