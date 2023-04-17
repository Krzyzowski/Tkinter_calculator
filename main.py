def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "stopni Celsjusza to ", fahrenheit, "stopni fahrenheita")
    return fahrenheit

f = cToF(20)

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    print(fahrenheit, "\xB0 fahrenheita to ", celsius, "\xB0 celsjusza")
    return celsius

c = fToC(150)

