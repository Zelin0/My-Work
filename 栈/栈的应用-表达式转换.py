from mod.pythonds.basic.stack import Stack

def infixropstfix(infixexpr):     #中缀转后缀
    prec = {}
    prec["*"] = 3    #记录操作符优先级
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixlist = []
    tokenlist = infixexpr.split() #解析表达式到单词列表


    for token in tokenlist:
        if token in "ABCDEFGHIJKLLMNOPQRSTUVWXYZ" or token in "0123456789": #操作数
            postfixlist.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfixlist.append(topToken)
                topToken = opstack.pop()
        else:           #操作符
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())
    return " ".join(postfixlist)

print(infixropstfix("A + B * C"))
print(infixropstfix("A * B + C"))
