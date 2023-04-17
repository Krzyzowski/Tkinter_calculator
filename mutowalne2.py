

def calcBasketValue(basketList):
    basketSum = 0
    for key in basketList:
        basketSum += basketList[key]
    return basketSum

shoppingBasket = {
    "smartphone" : 1200,
    "TV" : 1500,
    "console" : 1500
}

print( calcBasketValue(shoppingBasket)  )

def addNum(a,b):
    return a + b

value1 = addNum(10,5)
print( value1)

def 