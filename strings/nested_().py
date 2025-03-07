def max_nested_paranthesis(s):
    stack = []

    length = []
    for i in s:
        if i == "(":

            stack.append(i)
        if i == ")":
            length.append(len(stack))
            stack.pop()
    return max(length)

print(max_nested_paranthesis("(1+(2*3)+((8)/4))+1"))