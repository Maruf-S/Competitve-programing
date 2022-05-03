def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for i in tokens:
        if i == "+":
            stack.append(stack.pop() + stack.pop())
        elif i =="-":
            stack.append(-stack.pop()+ stack.pop())
        elif i == "*":
            stack.append(stack.pop()*stack.pop())
        elif i == "/":
            num1 = stack.pop()
            stack.append(stack.pop()//num1)
        else:
            stack.append(int(i))
    return stack[0]
print(evalRPN(["4","13","5","/","+"]))