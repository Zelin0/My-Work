from mod.pythonds.basic.stack import Stack

def parchecker(symbolString):
    s = Stack()

    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balanced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def match(top,symbol):
    opens = "([{"
    closers = ")]}"
    return opens.index(top) == closers.index(symbol)

print(parchecker('(()()())')) #嵌套加并列的括号
print(parchecker('((()))'))  #嵌套的括号
print(parchecker('(()'))
print(parchecker('()()()'))  #并列的括号
print(parchecker('()))((()')) #数量相等但错误
print(">>>>>>")

print(parchecker('{{([][])}()}'))
print(parchecker('[{()]'))
