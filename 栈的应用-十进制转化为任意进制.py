from mod.pythonds.basic.stack import Stack

def divedeBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString


def baseConverter(decNumber,base):
    digitals = "0123456789ABCEDF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digitals[remstack.pop()]

    return newString

print(divedeBy2(42))
print(">>>>>")
print(baseConverter(25,2))
print(baseConverter(25,16))
