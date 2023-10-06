test = 5
test2 = 7

def Add(*args):
    result = 0
    for x in args:
        result += x
    return result

def Subtract(x, y):
    return x - y

def Divide(x, y):
    if(y == 0):
        raise ValueError("Can not divide by zero")
    return x / y

def Multiply(x, y):
    return x * y
    

print(Add(test, test2, 6, 8))
print(Subtract(test, test2))
print(Multiply(5, 25))

try:
    print(Divide(5, 0))
except:
    print("Tried to divide by zero, oopsie!")