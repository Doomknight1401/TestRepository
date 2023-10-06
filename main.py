test = 5
test2 = 7

def AddNumbers(*args):
    result = 0
    for x in args:
        result += x
    return result

print(AddNumbers(test, test2, 6, 8))
